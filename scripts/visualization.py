import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV results
countries = pd.read_csv("/Users/abdullahaderinto/Documents/Netflix-Content-Insights/outputs/countries.csv")
genre = pd.read_csv("/Users/abdullahaderinto/Documents/Netflix-Content-Insights/outputs/genre.csv")
growth = pd.read_csv("/Users/abdullahaderinto/Documents/Netflix-Content-Insights/outputs/growth.csv")

# --- 1. Bar Chart: Top Countries ---
plt.figure(figsize=(10, 6))
plt.barh(countries["country"], countries["total_titles"], color="skyblue")
plt.gca().invert_yaxis()  # To show the highest bar on top
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Total Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("outputs/top_countries.png")
plt.close()

# --- 2. Pie Chart: Genre Distribution ---
plt.figure(figsize=(8, 8))
plt.pie(genre["total_titles"], labels=genre["genre"], 
        autopct='%1.1f%%', startangle=140)
plt.title("Top 10 Netflix Genres (Distribution)")
plt.tight_layout()
plt.savefig("outputs/genre_distribution.png")
plt.close()

# --- 3. Line Chart: Yearly Title Growth ---
plt.figure(figsize=(10, 6))
plt.plot(growth["release_year"], growth["total_titles"], marker='o', color="coral")
plt.title("Netflix Titles Released Per Year")
plt.xlabel("Year")
plt.ylabel("Total Titles")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("outputs/yearly_growth.png")
plt.close()


