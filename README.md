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

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/netflix-content-insights.git
cd netflix-content-insights

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows
