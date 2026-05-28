# Real-world Data Project (Retail Sales Analysis)
# Name: Naman Sanadhya

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("------ Real World Data Project ------")

# Load dataset
df = pd.read_csv("retail_sales.csv")

# Display records
print("\nFirst 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Total sales calculation
total_sales = df["Sales_Amount"].sum()

print("\nTotal Sales:", total_sales)

# Category-wise sales
category_sales = df.groupby("Category")["Sales_Amount"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

# Monthly sales graph
plt.figure(figsize=(8,5))

sns.lineplot(
    x="Month",
    y="Sales_Amount",
    data=df
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")

plt.show()

# Category sales graph
plt.figure(figsize=(8,5))

sns.barplot(
    x="Category",
    y="Sales_Amount",
    data=df
)

plt.title("Sales by Category")

plt.show()

# Profit distribution
plt.figure(figsize=(8,5))

plt.hist(df["Profit"])

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.show()

# Heatmap
plt.figure(figsize=(8,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()

print("\nObservations:")
print("1. Retail sales data was analyzed.")
print("2. Monthly sales trends were identified.")
print("3. Category performance was compared.")
print("4. Correlations between variables were studied.")
print("5. Visual insights were generated.")

print("\nProject Completed Successfully")