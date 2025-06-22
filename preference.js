//   function submitForm(){
//     document.addEventListener("DOMContentLoaded", function () {
//       document.getElementById("preferences-form").addEventListener("submit", async (e) => {
//         e.preventDefault();

//         const urlParams = new URLSearchParams(window.location.search);
//         const hotel = urlParams.get("hotel") || "";
//         const place = urlParams.get("place") || "";

//         const data = {
//           hotel,
//           place,
//           adults: +document.getElementById("adults").value || 0,
//           children: +document.getElementById("children").value || 0,
//           elderly: +document.getElementById("elderly").value || 0,
//           minBudget: document.getElementById("minBudget").innerText || 0,
//           maxBudget: document.getElementById("maxBudget").innerText || 0,
//           style: document.querySelector('input[name="vibe"]:checked')?.value || "Chill"
//         };

//         try {
//           const res = await fetch("/generate-plan", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify(data)
//           });

//           const json = await res.json();

//           // document.getElementById("response").innerText = json.plan;
//         window.location.href = "/planner";
//         } catch (err) {
//           console.error("Error:", err);
//           document.getElementById("response").innerText = "Error: Could not generate plan.";
//         }
//       });
//   // });
// });
  
// };

// 1. Define the function first
function submitForm() {
  document.getElementById("preferences-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const urlParams = new URLSearchParams(window.location.search);
    const hotel = urlParams.get("hotel") || "";
    const place = urlParams.get("place") || "";
    

    const data = {
      hotel: hotel !== "null" ? hotel : "",
      place: place !== "null" ? place : "",
      adults: +document.getElementById("adults").value || 0,
      children: +document.getElementById("children").value || 0,
      elderly: +document.getElementById("elderly").value || 0,
      minBudget: +document.querySelector("input[name='minBudget']").value || 0,
      maxBudget: +document.querySelector("input[name='maxBudget']").value || 0,
      style: document.querySelector('input[name="vibe"]:checked')?.value || "Chill"
    };

    if (!data.hotel) {
      alert("Missing hotel or place info. Please go back and select a valid location.");
      return;
    }

    try {
      const res = await fetch("/generate-plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      const json = await res.json();
      window.location.href = "/planner";
    } catch (err) {
      console.error("Error:", err);
      alert("Error: Could not generate plan.");
    }
  });
}

// 2. Then call it only once DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  submitForm();
});
