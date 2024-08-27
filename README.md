# baby-name-project-4
KU Boot Camp Project 4

Add a note on why we only have a few commits

## Overview

This project analyzes popular baby names by sex and ethnic group in New York City. The data, collected through civil birth registration, was last updated on June 15, 2024. Each record represents the ranking of a baby name in order of frequency, providing insights into name popularity trends.

The dataset can be used to assess the popularity of names, but caution is advised when interpreting the rank of names with frequency counts close to 10, as rankings may fluctuate year to year.

The dataset includes baby names ranging from 2011 to 2021.

## Team White Cast

- Albert Lee
- Jay Singh
- Austen Ortmeier
- Ryan Fagan

## File Structure

1. **Code Directory**
   - `02_Transform.ipynb`: Data preprocessing
   - `03_Load.ipynb`: Loading data into MongoDB
   - `04_Research_Questions.ipynb`: Answering research questions

2. **Output Directory**
   - Contains cleaned CSV files of baby names data

3. **Resource Directory**
   - Contains the original dataset

4. **Test Code Directory**
   - `app.py`: Main application file that runs the Flask server and handles routes
   - **Static Directory**
     - **CSS Directory**: `style.css` - Defines the styling for the web application
     - **JS Directory**: `app.js` - Contains client-side JavaScript for interactive features
   - **Templates Directory**: `index.html` - The main HTML template for the web application

## Setup and Usage

To run the project and view it on your computer:

1. **Prerequisites**: 
   - Install Python and MongoDB

2. **Installation**:
   - Clone the repository: `git clone [repository-url]`

3. **Data Loading**:
   - Run the `03_Load.ipynb` notebook to load the collection into MongoDB

4. **Running the Application**:
   - Ensure MongoDB is running
   - Execute `app.py`

5. **Functionality**:
   - The application displays baby names in a dropdown menu
   - Selecting a name shows metadata and a visualization
   - A baby name generator using the Markov chain model is also included

> **📝 Note:** The Markov chain model for name generation analyzes the existing names in the dataset to understand the probability of one character following another. When generating a new name, it starts with a random character and then selects subsequent characters based on these probabilities. This process continues until a full name is generated. The result is a new name that statistically resembles the names in the original dataset. While this provides a good starting point for name generation, more advanced techniques like recurrent neural networks could potentially produce even better results in future iterations of the project.

## Data Sources

- Original dataset: [Popular Baby Names](https://catalog.data.gov/dataset/popular-baby-names)

## Research Questions and Findings

1. Popular female name for a particular year
2. Popular male name for a particular year
3. Popular female baby names for particular ethnicities
4. Popular male baby names for particular ethnicities
5. Popular first letter for female baby name
6. Popular first letter for male baby name
7. Popular female baby name for the decade
8. Popular male baby name for the decade
9. Average length of a female baby name
10. Average length of a male baby name

[Insert detailed answers to research questions here]

## Visualizations

Power BI was used for answering some research questions. Below are the dashboards created:

![Dashboard 1: Name Popularity Trends](images/dashboard1.png)

![Dashboard 2: Ethnic and Gender Distribution](images/dashboard2.png)

## License

[Specify the license under which this project is released]
