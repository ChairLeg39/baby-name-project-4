document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('nameForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const gender = document.getElementById('gender').value;
        const ethnicity = document.getElementById('ethnicity').value;
        
        d3.json('http://localhost:5000/generate_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({gender, ethnicity})
        }).then(data => {
            // Display results
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<h2>Generated Names:</h2>';
            resultsDiv.innerHTML += '<ul>' + data.generated_names.map(name => `<li>${name}</li>`).join('') + '</ul>';

            // Visualize data (example: simple bar chart of name lengths)
            const nameLengths = data.generated_names.map(name => name.length);
            
            const svg = d3.select("#visualization")
                .append("svg")
                .attr("width", 300)
                .attr("height", 200);

            svg.selectAll("rect")
                .data(nameLengths)
                .enter()
                .append("rect")
                .attr("x", (d, i) => i * 60)
                .attr("y", d => 200 - d * 10)
                .attr("width", 50)
                .attr("height", d => d * 10)
                .attr("fill", "steelblue");

        }).catch((error) => {
            console.error('Error:', error);
            document.getElementById('results').innerHTML = 'An error occurred while generating names.';
        });
    });
});