function predict() {
    // Get input values
    const bedrooms = document.getElementById("bedrooms").value;
    const bathrooms = document.getElementById("bathrooms").value;
    const sqft_living = document.getElementById("sqft").value;
    const sqft_lot = document.getElementById("lot").value;
    const yr_built = document.getElementById("year").value;
    
    // Validate inputs
    if (!bedrooms || !bathrooms || !sqft_living || !sqft_lot || !yr_built) {
        document.getElementById("result").innerHTML = 
            "<span style='color: red;'>Please fill in all fields!</span>";
        return;
    }
    
    // Show loading message
    document.getElementById("result").innerHTML = "Predicting...";
    
    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            bedrooms: parseFloat(bedrooms),
            bathrooms: parseFloat(bathrooms),
            sqft_living: parseFloat(sqft_living),
            sqft_lot: parseFloat(sqft_lot),
            yr_built: parseFloat(yr_built)
        })
    })
    .then(res => {
        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
    })
    .then(data => {
        document.getElementById("result").innerHTML =
            "Estimated Price: ₹ " + data.predicted_price.toLocaleString();
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerHTML =
            "<span style='color: red;'>Error: " + error.message + "</span>";
    });
}
