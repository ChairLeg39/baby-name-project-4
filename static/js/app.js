// Build the metadata panel
function buildMetadata(sample) {
  d3.json("baby_names.json").then((data) => {

    // get the metadata field
    const metadata = data.metadata;

    // Filter the metadata for the object with the desired sample number
    const resultArray = metadata.filter("First Name");
    const result = resultArray[0];

    // Use d3 to select the panel with id of `#sample-metadata`
    const PANEL = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    PANEL.html("");

    // Inside a loop, you will need to use d3 to append new
    // tags for each key-value in the filtered metadata.
    Object.entries(result).forEach(([key, value]) => {
      PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
    });
  });
}

// function to build both charts
function buildCharts(sample) {
  d3.json("baby_names.json").then((data) => {

    // Get the metadata
    const metadata = data.metadata;

    // Get the first name, count and gender
    const FirstName = result.FirstName;
    const Count = result.Count;
    const Gender = result.Gender;

    // Build a Bubble Chart
    const bubbleData = [{
      x: FirstName,
      y: Count,
      text: "First Name",
      mode: 'markers',
      marker: {
        size: Count,
        color: Gender,
        colorscale: 'Earth'
      }
    }];
    const bubbleLayout = {
      title: {
        text: "Baby Name Count By Gender",
      x: 0.05 
      },
      margin: {t: 30, l: 60},
      hovermode: "closest",
      xaxis: {title: "First Name"},
      yaxis: {title: "Total"},
      autosize: true,
    font: {family: "Calibri"}
    }

    // Render the Bubble Chart
    Plotly.newPlot("bubble", bubbleData, bubbleLayout);

  
  });
}

// Function to run on page load
// Use d3 to select the dropdown with id of `#selDataset`
function init() {
  const selector = d3.select('#selDataset')
  d3.json("baby_names.json").then((data) => {

    // Get the names field
    // Get the first sample from the list
    // Build charts and metadata panel with the first sample
    // Use the list of sample names to populate the select options
    // Hint: Inside a loop, you will need to use d3 to append a new
    // option for each sample name.
    const sampleNames = data.names;
    sampleNames.forEach((sample) => {
          selector
                .append("option")
                .text(sample)
                .property("value", sample);
        });
      
        const firstSample = sampleNames[0];
        buildCharts(firstSample);
        buildMetadata(firstSample);
    });
}

// Function for event listener
// Build charts and metadata panel each time a new sample is selected
function optionChanged(newSample) {
  buildCharts(newSample);
  buildMetadata(newSample);
}
// Initialize the dashboard
init();
