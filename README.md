Population Distribution Analysis – Task 01

This project is part of the  SkillCraft Technology Task to visualize the distribution of a continuous variable — in this case, the population of countries using data from the **World Bank**.

Task Description

Task 01:**  
> Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

---

Dataset Used

- Source: [World Bank – Total Population (SP.POP.TOTL)](https://data.worldbank.org/indicator/SP.POP.TOTL)
- Sampled population data for 20 countries (year: 2020)



Tools & Libraries

Python 3.13.5
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [VS Code](https://code.visualstudio.com/)

---

Visualizations Included

1. Histogram of Country Populations (Log Scale)

- Shows how countries vary in population size.
- Uses log scale for better distribution visualization.

2. Bar Chart – Countries Grouped by Population Category

- Categories: `<10M`, `10–50M`, `50–100M`, `100–500M`, `500M–1B`, `>1B`
- Shows how many countries fall into each group.

---

Files Included

- `population_analysis.py` – Main Python script
- `population_histogram.png` *(optional)* – Histogram plot
- `population_barchart.png` *(optional)* – Bar chart plot

---

Learnings

- How to visualize continuous variable distributions
- Logarithmic histograms for skewed population data
- Grouping and binning for category-based bar charts

---
How to Run

```bash
# Clone the repo (replace with your repo URL)
git clone https://github.com/your-username/popu
