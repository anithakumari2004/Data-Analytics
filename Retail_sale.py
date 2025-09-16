#1. Setup, Data Loading, and Cleaning
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")


file_path = r"C:\Users\anita\OneDrive\Desktop\retail_sales_dataset.csv"


try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file was not found at the path: {file_path}")
    print("Please make sure the file path is correct and the file exists.")
    
    df = pd.DataFrame()
if not df.empty:
    print("\n--- DataFrame Head ---")
    print(df.head())

    print("\n--- DataFrame Info ---")
    df.info()

    # --- Data Cleaning ---

    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
        print("\n'Date' column converted to datetime format.")


    duplicates = df.duplicated().sum()
    print(f"\nFound {duplicates} duplicate rows.")
    df.drop_duplicates(inplace=True)
    print("Duplicate rows have been removed.")

    print("\n--- Cleaned DataFrame Info ---")
    df.info()
# 2. Descriptive Statistics

print("--- Descriptive Statistics ---")
print(df.describe().T)
if 'Sales' in df.columns:
    print(f"\nMean Sales: ${df['Sales'].mean():.2f}")
    print(f"Median Sales: ${df['Sales'].median():.2f}")
    print(f"Standard Deviation of Sales: ${df['Sales'].std():.2f}")
    
if 'City' in df.columns:
    print("\n--- Sales by City ---")
    print(df['City'].value_counts())
    
# 3. Time Series Analysis 

df_time = df.set_index('Date')
monthly_sales = df_time['Total Amount'].resample('M').sum()

print("--- Total Sales per Month ---")
print(monthly_sales)
plt.figure(figsize=(12, 6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title('Total Sales Over Time (Monthly)')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# 4. Customer and Product Analysis

top_customers = df.groupby('CustomerID')['Sales'].sum().sort_values(ascending=False).head(10)
print("--- Top 10 Customers by Sales ---")
print(top_customers)

top_products = df.groupby('ProductID')['Sales'].sum().sort_values(ascending=False).head(10)
print("\n--- Top 10 Products by Sales ---")
print(top_products)

if 'City' in df.columns:
    sales_by_city = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
    print("\n--- Total Sales by City ---")
    print(sales_by_city)
    
# 5. Visualization
# --- Bar Chart for Top Products ---
plt.figure(figsize=(12, 7))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis', orient='h')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Total Sales')
plt.ylabel('Product ID')
plt.show()

# --- Histogram for Sales Distribution ---
plt.figure(figsize=(10, 6))
sns.histplot(df['Sales'], bins=30, kde=True)
plt.title('Distribution of Sales Amount per Transaction')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()

# --- Bar Chart for Sales by City ---
if 'City' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.barplot(x=sales_by_city.index, y=sales_by_city.values, palette='plasma')
    plt.title('Total Sales by City')
    plt.xlabel('City')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.show()









