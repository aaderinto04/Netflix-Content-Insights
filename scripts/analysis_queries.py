import sqlite3
import pandas as pd

conn = sqlite3.connect("netflix.db")

#Top 10 countries that produce the most content
query1 = """
SELECT 
country, COUNT(*) AS total_titles
FROM netflix
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10 ;"""

query1_res = pd.read_sql_query(query1, conn)
print(query1_res)

query2 = """
SELECT 
listed_in AS genre, COUNT(*) AS total_titles
FROM netflix
WHERE listed_in IS NOT NULL
GROUP BY genre
ORDER BY total_titles DESC
LIMIT 10 ;"""

query2_res = pd.read_sql_query(query2, conn)
print(query2_res)

query3 = """
SELECT 
release_year, COUNT(*) AS total_titles
FROM netflix
WHERE release_year IS NOT NULL
GROUP BY release_year
ORDER BY release_year;"""

query3_res = pd.read_sql_query(query3, conn)
print(query3_res)

countries = pd.read_sql(query1, conn)
genre = pd.read_sql(query2, conn)
growth = pd.read_sql(query3, conn)

countries.to_csv("/Users/abdullahaderinto/Documents/Netflix-Content-Insights/outputs/countries.csv")
genre.to_csv("/Users/abdullahaderinto/Documents/Netflix-Content-Insights/outputs/genre.csv")
growth.to_csv("/Users/abdullahaderinto/Documents/Netflix-Content-Insights/outputs/growth.csv")