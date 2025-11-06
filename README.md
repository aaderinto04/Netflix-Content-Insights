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

## Project Structure
netflix_insights/
│
├── data/
│ └── netflix_titles.csv # Dataset from Kaggle
│
├── scripts/
│ ├── create_db.py # Loads CSV data into SQLite database
│ ├── analysis_queries.py # Runs SQL queries and saves results
│ └── visualization.py # Creates charts from query outputs
│
├── outputs/
│ ├── countries.csv
│ ├── genre.csv
│ ├── growth.csv
│ ├── top_countries.png
│ ├── genre_distribution.png
│ └── yearly_growth.png
│
└── README.md


---

## Dataset
**Source:** [Kaggle — Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

**Columns include:**  
`show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description`

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/netflix-content-insights.git
cd netflix-content-insights
