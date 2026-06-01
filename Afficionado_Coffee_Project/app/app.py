import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(
    page_title="Afficionado Coffee Roasters Dashboard",
    layout="wide"
)

st.title("☕ Afficionado Coffee Roasters")
st.subheader("Sales Trend and Time-Based Performance Analysis")

# Load Data
df = pd.read_csv("../data/coffee_sales.csv")

# Feature Engineering
df['revenue'] = df['transaction_qty'] * df['unit_price']

df['transaction_time'] = pd.to_datetime(
    df['transaction_time'],
    format='%H:%M:%S'
)

df['hour'] = df['transaction_time'].dt.hour

# KPIs
total_revenue = df['revenue'].sum()

hourly_sales = df.groupby('hour')['revenue'].sum()
peak_hour = hourly_sales.idxmax()
peak_revenue = hourly_sales.max()

store_sales = df.groupby('store_location')['revenue'].sum()
top_store = store_sales.idxmax()

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Peak Revenue Hour", f"{peak_hour}:00")
col3.metric("Top Store", top_store)

# Sidebar Filter
st.sidebar.header("Filters")

selected_store = st.sidebar.selectbox(
    "Select Store",
    ["All"] + list(df['store_location'].unique())
)

if selected_store != "All":
    filtered_df = df[df['store_location'] == selected_store]
else:
    filtered_df = df

# Hourly Revenue Chart
st.subheader("Hourly Revenue Analysis")

hourly_sales_filtered = filtered_df.groupby('hour')['revenue'].sum()

fig, ax = plt.subplots(figsize=(10,4))
hourly_sales_filtered.plot(kind='bar', ax=ax)

ax.set_xlabel("Hour")
ax.set_ylabel("Revenue")
ax.set_title("Hourly Revenue")

st.pyplot(fig)

# Store Revenue Chart
st.subheader("Store Wise Revenue")

store_sales_filtered = filtered_df.groupby(
    'store_location'
)['revenue'].sum()

fig2, ax2 = plt.subplots(figsize=(8,4))
store_sales_filtered.plot(kind='bar', ax=ax2)

ax2.set_xlabel("Store Location")
ax2.set_ylabel("Revenue")

st.pyplot(fig2)

# Heatmap
st.subheader("Store Location vs Hourly Revenue Heatmap")

heatmap_data = df.pivot_table(
    values='revenue',
    index='store_location',
    columns='hour',
    aggfunc='sum'
)

fig3, ax3 = plt.subplots(figsize=(12,5))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu",
    ax=ax3
)

st.pyplot(fig3)

# Final Insights
st.subheader("Key Insights")

st.write("✅ Peak Revenue Hour: 10 AM")
st.write("✅ Peak Transaction Hour: 10 AM")
st.write("✅ Top Store Location: Hell's Kitchen")
st.write("✅ Morning hours generate maximum sales")
st.write("✅ Revenue declines after 11 AM")
