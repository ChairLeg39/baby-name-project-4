// Connect to Flask API
var url = "/sourcedata"; // Baby Names

// Fetch the JSON data and console log it
d3.json(url).then(function(data) {
  console.log(data);
});

// Initialize the dashboard at start up
function init() {
    d3.json(url).then(data => {
        console.log(data);
        
        // Extract unique genders and ethnicities
        let genders = [...new Set(data.map(item => item.Gender))];
        let ethnicities = [...new Set(data.map(item => item.Ethnicity))];
        
        // Populate dropdown menus
        populateDropdown("#selGender", genders);
        populateDropdown("#selEthnicity", ethnicities);
    });
}

function populateDropdown(selector, options) {
    let dropdown = d3.select(selector);
    options.forEach(option => {
        dropdown.append("option")
            .text(option)
            .property("value", option);
    });
}

function optionChanged() {
    let selectedGender = d3.select("#selGender").property("value");
    let selectedEthnicity = d3.select("#selEthnicity").property("value");
    
    console.log("Selected Gender:", selectedGender);
    console.log("Selected Ethnicity:", selectedEthnicity);

    // Call function to update charts/visualizations
    updateCharts(selectedGender, selectedEthnicity);
}

// Used trained models to generate names
function generateName() {
    let selectedGender = d3.select("#selGender").property("value");
    let selectedEthnicity = d3.select("#selEthnicity").property("value");
    
    fetch('/generate_name', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            gender: selectedGender,
            ethnicity: selectedEthnicity
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.name) {
            d3.select("#generatedName").text(data.name + " (AI-generated)");
        } else {
            d3.select("#generatedName").text("Unable to generate name");
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        d3.select("#generatedName").text("Error generating name");
    });
}

// Call the initialize function to initialize the dashboard
init();