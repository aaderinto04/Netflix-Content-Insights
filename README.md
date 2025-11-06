# Netflix-Content-Insights

## Overview
The Netflix Content Insights Dashboard is a Python-based data analytics project designed to explore patterns within Netflix’s catalog.  
Using Pandas, SQLite, and Matplotlib, the project extracts and visualizes insights about content distribution, genre popularity, and yearly growth.  
All data analysis and visualization steps are automated through Python scripts.

---

## Tech Stack
- **Python** — data processing and automation  
- **Pandas** — data manipulation and analysis  
- **SQLite** — relational database for structured querying  
- **Matplotlib** — static visualizations  

---




---

## Dataset
**Source:** [Kaggle — Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

**Columns include:**  
`show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description`

---

How to Run
1. Clone the Repository
git clone https://github.com/yourusername/netflix-content-insights.git
cd netflix-content-insights

2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows

3. Install Dependencies
pip install -r requirements.txt


Main Libraries Used:

pandas

matplotlib

sqlite3 (built-in)

4. Load the Dataset into SQLite

Run the load_data.py script to import the dataset into a local SQLite database.

python load_data.py


This script will:

Create a local database file named netflix.db

Load the Netflix CSV dataset into a table named netflix_titles

5. Run SQL Analysis Queries

Open and execute analysis_queries.sql in a SQL client or Python.

Includes queries for:

Top producing countries

Genre distribution

Yearly title growth

Example (run from terminal):

sqlite3 netflix.db < analysis_queries.sql

6. Visualize Insights with Python

Run the visualization script to generate charts using Matplotlib.

python visualize_results.py


Outputs:

top_countries.png — Bar chart of countries with most titles

genre_distribution.png — Pie chart showing genre breakdown

yearly_growth.png — Line chart of content growth by year

