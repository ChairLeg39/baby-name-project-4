
console.log("post.js loaded")
let submit = d3.select("#submit");

submit.on("click", () => {
    let year_born = d3.select("#year_born").node().value;
    let gender = d3.select("#gender").node().value;
    let ethnicity = d3.select("#ethnicity").node().value;
    
    let response = d3.select("#response");

    payload = { data: [parseInt(hp), parseInt(attack), parseInt(defense), parseInt(special_attack), parseInt(special_defense), parseInt(speed)] }

    d3.text("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "data=" + JSON.stringify(payload) // add it to the http header as a json string
    }).then(data => {
        //display the data in div 'response'
        response.text(`${data} ${response.text()}`)
        //log the data
        console.log('this is what the response from flask was')
        console.log(data);
    });
});
