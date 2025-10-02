import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Country Name": ["India", "China", "USA", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico",
                     "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", "Germany", "Turkey", "France", "UK", "Italy"],
    "2020": [1380004385, 1439323776, 331002651, 273523615, 212559417, 220892340, 206139589, 164689383, 145934462, 128932753,
             126476461, 114963588, 109581078, 102334404, 97338579, 83783942, 84339067, 65273511, 67886011, 60461826]
}


df = pd.DataFrame(data)


year = "2020"
df["Population"] = df[year]


plt.figure(figsize=(10, 6))
bins = np.logspace(np.log10(df["Population"].min()), np.log10(df["Population"].max()), 10)
plt.hist(df["Population"], bins=bins, edgecolor="black")
plt.xscale("log")
plt.xlabel("Country Population (log scale)")
plt.ylabel("Number of Countries")
plt.title(f"Distribution of Country Populations in {year}")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

category_bins = [0, 1e7, 5e7, 1e8, 5e8, 1e9, 2e9]
labels = ["<10M", "10–50M", "50–100M", "100–500M", "500M–1B", ">1B"]
df["Pop_Category"] = pd.cut(df["Population"], bins=category_bins, labels=labels, include_lowest=True)

cat_counts = df["Pop_Category"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
sns.barplot(x=cat_counts.index, y=cat_counts.values, palette="viridis")
plt.xlabel("Population Category")
plt.ylabel("Number of Countries")
plt.title(f"Number of Countries by Population Category ({year})")
plt.tight_layout()
plt.show()
