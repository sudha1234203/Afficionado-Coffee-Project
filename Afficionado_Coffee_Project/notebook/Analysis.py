import pandas as pd

df = pd.read_csv("data/coffee_sales.csv")

# Revenue Column
df['revenue'] = df['transaction_qty'] * df['unit_price']

# Convert Time Column
# Convert Time Column
df['transaction_time'] = pd.to_datetime(
    df['transaction_time'],
    format='%H:%M:%S'
)

# Extract Hour
df['hour'] = df['transaction_time'].dt.hour

# Extract Day Name
df['day_of_week'] = df['transaction_time'].dt.day_name()

print(df[['transaction_time', 'hour', 'day_of_week', 'revenue']].head())

# # Revenue by Day of Week

# day_sales = df.groupby('day_of_week')['revenue'].sum()

# print("\nRevenue By Day:\n")
# print(day_sales)

# Hourly Revenue Analysis

hourly_sales = df.groupby('hour')['revenue'].sum()

print("\nHourly Revenue:\n")
print(hourly_sales)



# Peak Revenue Hour

peak_hour = hourly_sales.idxmax()
peak_revenue = hourly_sales.max()

print("\nPeak Revenue Hour:")
print(f"Hour: {peak_hour}")
print(f"Revenue: {peak_revenue}")

import matplotlib.pyplot as plt

hourly_sales.plot(kind='bar')

plt.title("Hourly Revenue Analysis")
plt.xlabel("Hour")
plt.ylabel("Revenue")

plt.show()

# =========================
# Store Wise Revenue Analysis
# =========================

store_sales = df.groupby('store_location')['revenue'].sum()

print("\nStore Wise Revenue:\n")
print(store_sales.sort_values(ascending=False))

top_store = store_sales.idxmax()
top_store_revenue = store_sales.max()

print("\nTop Performing Store:")
print(f"Store: {top_store}")
print(f"Revenue: {top_store_revenue:.2f}")

# =========================
# Hourly Transactions
# =========================

hourly_transactions = df.groupby('hour')['transaction_id'].count()

print("\nHourly Transactions:\n")
print(hourly_transactions)

peak_transaction_hour = hourly_transactions.idxmax()

print(f"\nPeak Transaction Hour: {peak_transaction_hour}")

# =========================
# Day Wise Revenue Analysis
# =========================

day_sales = df.groupby('day_of_week')['revenue'].sum()

print("\nDay Wise Revenue:\n")
print(day_sales.sort_values(ascending=False))

top_day = day_sales.idxmax()
top_day_revenue = day_sales.max()

print("\nBest Revenue Day:")
print(f"Day: {top_day}")
print(f"Revenue: {top_day_revenue:.2f}")

# =========================
# Day Wise Revenue Chart
# =========================

plt.figure(figsize=(8,5))

day_sales.plot(kind='bar')

plt.title("Revenue by Day of Week")
plt.xlabel("Day")
plt.ylabel("Revenue")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# =========================
# Heatmap Analysis
# =========================

import seaborn as sns

heatmap_data = df.pivot_table(
    values='revenue',
    index='store_location',
    columns='hour',
    aggfunc='sum'
)

print("\nHeatmap Data:\n")
print(heatmap_data)

plt.figure(figsize=(12,5))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu"
)

plt.title("Store Location vs Hourly Revenue Heatmap")
plt.xlabel("Hour")
plt.ylabel("Store Location")

plt.tight_layout()
plt.show()

# =========================
# Final Project Summary
# =========================

print("\n========== FINAL PROJECT INSIGHTS ==========")

print(f"\nPeak Revenue Hour : {peak_hour}:00")
print(f"Revenue Generated : {peak_revenue:.2f}")

print(f"\nPeak Transaction Hour : {peak_transaction_hour}:00")

print(f"\nTop Store Location : {top_store}")
print(f"Revenue Generated  : {top_store_revenue:.2f}")

print(f"\nBest Revenue Day : {top_day}")
print(f"Revenue Generated : {top_day_revenue:.2f}")

print(df.columns.tolist())