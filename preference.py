from flask import Flask, request, jsonify, render_template, session
from dotenv import load_dotenv
from openai import OpenAI
import os
import re
from datetime import datetime


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/choose_place")
def choose_place():
    return render_template("choose_place.html")

@app.route("/after_penang")
def after_penang():
    return render_template("after_penang.html")

@app.route("/after_sabah")
def after_sabah():
    return render_template("after_sabah.html")

@app.route("/hotel")
def hotel():
    return render_template("hotel.html")

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")

@app.route("/preference")
def preference():
    return render_template("preference.html")

@app.route("/planner")
def planner():
    plan = session.get("plan", {})
    place = session.get("selected_place", "penang")  # ✅ Now gets place from session
    return render_template("planner.html", plan=plan, place=place)

@app.route("/streetview")
def streetview():
    place = request.args.get("place", "penang")
    return render_template("streetview.html", place=place)

@app.route("/get-places/<place>")
def get_places(place):
    try:
        filename = f"places_{place}.txt"
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "File not found", 404

def parse_gpt_response(response_text):
    sections = {
        "places": "",
        "car": "",
        "summary": ""
    }

    try:
        parts = re.split(r"\d\.\s*", response_text)
        for part in parts:
            if "places to visit" in part.lower():
                sections["places"] = part.split(":", 1)[-1].strip()
            elif "suggested car rental" in part.lower():
                sections["car"] = part.split(":", 1)[-1].strip()
            elif "planner summary" in part.lower():
                sections["summary"] = part.split(":", 1)[-1].strip()
    except Exception as e:
        print("Error parsing GPT response:", e)

    return sections


@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    
    try:

        data = request.get_json()

        hotel = data.get("hotel", "").strip() or "a hotel you booked"
        place = data.get("place", "").strip() or "your selected destination"
        
        session["selected_place"] = place
        adults     = int(data.get("adults", 0))
        children   = int(data.get("children", 0))
        elderly    = int(data.get("elderly", 0))
        min_budget = data.get("minBudget", 0)
        max_budget = data.get("maxBudget", 0)
        style      = data.get("style", "Chill")

        num_days = 2

        prompt = f"""
        You are planning a {num_days}-day trip to {place} for {adults} adults, {children} children, and {elderly} elderly people. 
        The hotel the user has booked is **{hotel}**.
        The preferred travel style is "{style}" and the budget is RM {min_budget} to RM {max_budget}. 

        Please respond with the following structured section:
        1. Places to Visit:
        • (List 3-5 places in {{place}}.) Do not include descriptions.

        2. Suggested Car Rental:
        • Recommend a vehicle size/model and why.

        3. Planner Summary:
        • Write a {num_days}-day, day-by-day summary with recommended activities for each day.
        • For example:
            Day 1: Visit A, then go to B. Lunch at C...
            Day 2: Morning at D, relax at E, etc.
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful travel planner."},
                {"role": "user",   "content": prompt}
            ]
        )

        response_text = response.choices[0].message.content
        sections = parse_gpt_response(response_text)

        session["plan"] = sections
        print("✅ Session data saved:", session["plan"])
        
        # Save to text files
        with open("places_penang.txt", "w", encoding="utf-8") as f:
            f.write(sections["places"])

        return jsonify({"plan": response_text})
    
    except Exception as e:
        print("Error:", repr(e))
        return jsonify({"plan": "Sorry, something went wrong generating your travel plan."}), 500

if __name__ == "__main__":
    app.run(debug=True)
