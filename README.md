# Deepsick

# Project Title 
CutiBuddy


# Project Description
CutiBuddy is a smart plug-in, mobile app designed that enhance travel booking platforms. It automatically generates personalized, AI-powered travel itineraries based on the user’s hotel location, travel style, group size and budget. 

The app features an interactive Street View map with avatar narrators that introduce the cultural and historical stories of each destination. This experience increases user engagemnt after booking and promotes sustainable, culture-rich tourism, supporting initiatives like Visit Malaysia 2026.


# Team Members
- Denise Ong Zie Rui - Integrate character dialogue into Google Street View
- Khor Chia Yuan - Develop landmark mapping and Google Street View integration
- Liew Chew Ling - Build the Travel Preferences page
- Mandy Kok Fei Li - Integrate AI to generate personalized travel itineraries
- Yap Shin Yi- Designed the overall UI/UX of the app


# Technologies Used
- Frontend: HTML, CSS, Javascript
- Backend: Python(Flask)
- APIs: Google Maps API, Street View API, OpenAI API
- Data/Configuration Files: JSON and TXT files
- Others: Bootstrap


# Challenges & Approach
Challenges:
    1. Travel Pain Points
    Travelers often struggle to plan culturally meaningful trips due to scattered and unstructured information:
        - Cultural itineraries are rarely provided during the booking process, leaving travelers with generic plans.
        - Users must browse multiple sources like blogs, TikTok and review sites to discover local experiences.
        - The process is time-consuming, often causing travelers to miss out opportunities for valuable cultural discovery.

    2. Platform Pain Points
    Travel platforms face barriers in delivering personalized, culture-driven experiences:
        - Developing and managing an AI-based itinerary system requires high investment in time and resources.
        - Relying on third-party integrations limits flexibility, customization and overall control of the user experience.

Approach: 
    To address these challenges, we developed a smart plug-in mobile app that integrates directly with travel booking platforms to enhance the post-booking experience. The app offers two key features:

    1. AI-Powered Cultural Itinerary Generation
    - Travelers input essential details such as travel style, group size and budget. Based on these information, the system generates a personalized day-by-day itinerary focused on cultural experiences and attractions near the user’s booked accommodation.

    2. Interactive Cultural Map with Avatar Narration
    - The itinerary is visualized on an interactive map. Travelers can click on each location to launch Google Street View, where a virtual avatar delivers rich historical and cultural narratives of the site. This transforms the itinerary into a guided, immersive digital heritage experience.


# Usage Instructions
! Important: Remember to replace the placeholder API key with your own valid Google Maps API keys in the HTML files before running the application.

1. Launch the App (using Flask)
    - Open a terminal and navigate to the project folder.
    - Run the following command to start the Flask server: python preference.py
    - This will start a local server and automatically load the main landing page (index.html) in your browser.
    - Click the blue arrow button (→) to begin your travel journey.

2. Choose Your Destination (choose_place.html)
    - Select your preferred travel destination: Penang or Sabah.
    - Click the “Discover” button to proceed.

3. Destination Details (after_penang.html or after_sabah.html)
    - If you selected Penang, you’ll be redirected to after_penang.html.
    - Click the "Book Now" button to proceed to the hotel booking process.

4. Hotel Booking Page (hotel.html)
    - Enter your accommodation details, such as hotel name, check-in/out dates, etc.
    - Click "Confirm Booking" to confirm your stay.

5. Trip Confirmation (confirm.html)
    - A confirmation popup will appear, asking whether you’d like to plan a trip.
    - Click "Yes, plan for me" to proceed to the preferences page.

6. Set Your Trip Preferences (preference.html)
    - Choose your number of travelers, budget range and travelling style.
    - Click the "Generate" button to continue.

7. AI Itinerary Planner (planner.html)
    - ThAn AI-generated day-by-day itinerary will be created based on your preferences and hotel location.
    - The itinerary includes places to visit, Suggested Car Rental, Trip Summary.

8. Explore Interactive Map (planner.html → viewMaps)
    - On the itinerary page, click "Explore Street View" to explore your destinations visually.
    - You’ll be redirected to a live Google Map featuring all your itinerary points.

9. Landmark Street View (streetview.html)
    - The map shows all suggested landmarks and attractions.
    - Click on any location marker to view an immersive Google Street View right on the same page.

10. Virtual Avatar Experience (streetview.html)
    - Here, you’ll step into a guided Street View tour enhanced with a virtual avatar narrator.
    - The avatar will shares historical facts, cultural stories, and insights about each destination.
    - Click the "Back" button to return to the map and explore more landmarks.



