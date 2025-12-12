# ======================================================
# ADVANCED DATA VISUALIZATION PROJECT
# ======================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ======================================================
# 1. LOAD DATA
# ======================================================
df = pd.read_csv("sales_data.csv")

print("\n==============================================")
print("              DATA LOADED SUCCESSFULLY")
print("==============================================\n")
print(df.head())


# ======================================================
# 2. BASIC OVERVIEW
# ======================================================
print("\n================ BASIC INFO ===============\n")
print(df.info())

print("\n================ DESCRIPTIVE STATS ===============\n")
print(df.describe())


# ======================================================
# 3. SALES TREND (LINE CHART)
# ======================================================
plt.figure(figsize=(10,5))
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("sales_trend.png")
plt.show()


# ======================================================
# 4. CATEGORY-WISE SALES (BAR CHART)
# ======================================================
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,4))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig("category_sales.png")
plt.show()


# ======================================================
# 5. SALES DISTRIBUTION (HISTOGRAM)
# ======================================================
plt.figure(figsize=(8,4))
sns.histplot(df['Sales'], bins=20, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("sales_distribution.png")
plt.show()


# ======================================================
# 6. PROFIT COMPARISON (BOXPLOT)
# ======================================================
plt.figure(figsize=(8,4))
sns.boxplot(x=df["Profit"])
plt.title("Profit Distribution")
plt.savefig("profit_boxplot.png")
plt.show()


# ======================================================
# 7. SALES vs PROFIT (SCATTER PLOT)
# ======================================================
plt.figure(figsize=(8,4))
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Sales vs Profit Relationship")
plt.savefig("sales_profit_scatter.png")
plt.show()


# ======================================================
# 8. CORRELATION HEATMAP
# ======================================================
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()


# ======================================================
# 9. PAIRPLOT (ADVANCED)
# ======================================================
sns.pairplot(df)
plt.savefig("pairplot.png")
plt.show()


# ======================================================
# 10. SUMMARY
# ======================================================
print("\n================ SUMMARY REPORT ===============\n")
print("Total Records:", len(df))
print("Total Categories:", df['Category'].nunique())
print("Highest Sales:", df['Sales'].max())
print("Highest Profit:", df['Profit'].max())

print("\nVisualizations saved as PNG files.")
print("Dashboard completed successfully!")
