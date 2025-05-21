import streamlit as st
import pandas as pd
from utils import load_data

# Load data
combined_df, country_dfs = load_data()

# Streamlit UI
st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("🌞 Solar Potential Dashboard")

# Sidebar
st.sidebar.header("Select a Country")
selected_country = st.sidebar.selectbox("Country", country_dfs.keys())

# Show filtered data
st.subheader(f"{selected_country} - Solar Data Preview")
st.dataframe(country_dfs[selected_country].head())

# Summary stats
st.subheader("📊 Summary Statistics")
st.write(country_dfs[selected_country].describe())

# Plot (optional)
st.subheader("☀️ Time Series / Trends (if available)")
if 'date' in country_dfs[selected_country].columns:
    df = country_dfs[selected_country].copy()
    df['date'] = pd.to_datetime(df['date'])
    st.line_chart(df.set_index('date').select_dtypes(include='number'))
else:
    st.info("No time series column found for plotting.")
