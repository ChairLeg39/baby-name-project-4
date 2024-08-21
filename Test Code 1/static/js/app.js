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

// // Initialize the dashboard at start up
// function init() {
//     d3.json(url).then(data => {
        
//         // Extract unique genders
//         let genders = [...new Set(data.map(item => item.Gender))];
//         let dropdownMenuGender = d3.select("#selGender");

//         // Add genders to the dropdown menu
//         genders.forEach(gender => {
//             console.log(gender);
//             dropdownMenuGender.append("option")
//                 .text(gender)
//                 .property("value", gender);
//         });

//         // Extract unique ethnicities
//         let ethnicities = [...new Set(data.map(item => item.Ethnicity))];
//         let dropdownMenuEthnicity = d3.select("#selEthnicity");

//         // Add ethnicities to the dropdown menu
//         ethnicities.forEach(ethnicity => {
//             console.log(ethnicity);
//             dropdownMenuEthnicity.append("option")
//                 .text(ethnicity)
//                 .property("value", ethnicity);
//         });

//         // Extract the first gender and ethnicity
//         let firstGender = genders[0];
//         let firstEthnicity = ethnicities[0];

//         console.log("First Gender:", firstGender);
//         console.log("First Ethnicity:", firstEthnicity);

//         // You can call functions to build initial plots here
//         // updatePlots(firstGender, firstEthnicity);
//     });
// }

function optionChanged() {
    let selectedGender = d3.select("#selGender").property("value");
    let selectedEthnicity = d3.select("#selEthnicity").property("value");
    
    console.log("Selected Gender:", selectedGender);
    console.log("Selected Ethnicity:", selectedEthnicity);

    // Call function to update charts/visualizations
    updateCharts(selectedGender, selectedEthnicity);
}

function updateCharts(gender, ethnicity) {
    // Filter data based on selected gender and ethnicity
    // Update your charts or visualizations here
    // For example:
    // updateBarChart(gender, ethnicity);
    // updateLineChart(gender, ethnicity);
}

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
            d3.select("#generatedName").text(data.name);
        } else {
            d3.select("#generatedName").text("No matching names found");
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        d3.select("#generatedName").text("Error generating name");
    });
}

// Call the initialize function to initialize the dashboard
init();