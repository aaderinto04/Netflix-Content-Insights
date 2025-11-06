import pandas as pd
import sqlite3


df = pd.read_csv('/Users/abdullahaderinto/Documents/Netflix-Content-Insights/data/netflix_titles.csv')
print(df)

conn = sqlite3.connect('netflix.db')
df.to_sql("netflix", conn, if_exists="replace", index=False)

conn.close()