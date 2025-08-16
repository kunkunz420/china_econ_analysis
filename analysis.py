import pandas as pd
import matplotlib.pyplot as plt
import os

# Folder paths
data_path = "./data/"
output_path = "./output_figures/"
os.makedirs(output_path, exist_ok=True)

# === 1. Macroeconomic Indicators ===
macro = pd.read_csv(data_path + "annual_data.csv")
macro = macro.set_index("Indicator").T
macro.index.name = "Year"

# GDP & GNI trends
fig, ax = plt.subplots(figsize=(8, 5))
macro[["Gross Domestic Product (100 million yuan)", "Gross National Income (100 million yuan)"]].plot(ax=ax, marker="o")
plt.title("GDP and GNI (2015–2024)")
plt.ylabel("100 million yuan")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "gdp_gni.png")
plt.close()

# Value added by three industries
fig, ax = plt.subplots(figsize=(8, 5))
macro[[
    "Value Added of Primary Industry (100 million yuan)",
    "Value Added of Secondary Industry (100 million yuan)",
    "Value Added of Tertiary Industry (100 million yuan)"
]].plot(ax=ax, marker="o")
plt.title("Value Added by Industry (2015–2024)")
plt.ylabel("100 million yuan")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "industry_value_added.png")
plt.close()

# Per capita GDP
fig, ax = plt.subplots(figsize=(8, 5))
macro["Per Capita GDP (yuan)"].plot(ax=ax, marker="o")
plt.title("Per Capita GDP (2015–2024)")
plt.ylabel("yuan")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "per_capita_gdp.png")
plt.close()

# === 2. Per Capita Income ===
income = pd.read_csv(data_path + "per_capita_income_10y.csv")
income = income.set_index("Indicator").T
income.index.name = "Year"

# Mean and median income
fig, ax = plt.subplots(figsize=(8, 5))
income[[
    "Per Capita Disposable Income (yuan)",
    "Median Per Capita Disposable Income (yuan)"
]].plot(ax=ax, marker="o")
plt.title("Per Capita Income and Median (2015–2024)")
plt.ylabel("yuan")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "income_median_mean.png")
plt.close()

# Income structure
fig, ax = plt.subplots(figsize=(8, 5))
income[[
    "Per Capita Wage Income (yuan)",
    "Per Capita Net Operating Income (yuan)",
    "Per Capita Net Property Income (yuan)",
    "Per Capita Net Transfer Income (yuan)"
]].plot(ax=ax, marker="o")
plt.title("Income Structure (2015–2024)")
plt.ylabel("yuan")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "income_structure.png")
plt.close()

# === 3. Per Capita Expenditure ===
expend = pd.read_csv(data_path + "per_capita_expenditure_10y.csv")
expend = expend.set_index("Indicator").T
expend.index.name = "Year"

# Total expenditure and services
fig, ax = plt.subplots(figsize=(8, 5))
expend[[
    "Per Capita Consumption Expenditure (yuan)",
    "Per Capita Expenditure on Services (yuan)"
]].plot(ax=ax, marker="o")
plt.title("Consumption & Services Expenditure (2015–2024)")
plt.ylabel("yuan")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "total_services_expenditure.png")
plt.close()

# Main expenditure components
fig, ax = plt.subplots(figsize=(8, 5))
expend[[
    "Per Capita Expenditure on Food, Tobacco and Alcohol (yuan)",
    "Per Capita Expenditure on Housing (yuan)",
    "Per Capita Expenditure on Education, Culture and Recreation (yuan)",
    "Per Capita Expenditure on Health Care (yuan)"
]].plot(ax=ax, marker="o")
plt.title("Main Consumption Components (2015–2024)")
plt.ylabel("yuan")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "main_expenditure_components.png")
plt.close()

# === 4. Education Statistics ===
edu = pd.read_csv(data_path + "education_per_100k_10y.csv")
edu = edu.set_index("Indicator").T
edu.index.name = "Year"

# All education levels
fig, ax = plt.subplots(figsize=(8, 5))
edu.plot(ax=ax, marker="o")
plt.title("Number of Students per 100,000 (2015–2024)")
plt.ylabel("persons")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path + "education_levels.png")
plt.close()

print("All charts saved in the 'output_figures' folder.")
