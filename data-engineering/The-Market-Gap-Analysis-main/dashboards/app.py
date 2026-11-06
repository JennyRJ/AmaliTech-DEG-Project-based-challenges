import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Set the dashboard title
st.title("Sugar Trap: Market Gap Analysis")

st.write(
    "Exploring opportunities for high-protein, "
    "low-sugar food products."
)

# Locate the main project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the dashboard dataset
data_path = project_folder / "data" / "processed" / "dashboard_data.csv"

# Load the dataset
df = pd.read_csv(data_path)

# Display basic information
st.write("Total products analysed:", len(df))

st.write(
    "Opportunity products:",
    df["Opportunity"].sum()
)
st.subheader("Explore products by category")

categories = ["All Categories"] + sorted(
    df["Primary Category"].dropna().unique().tolist()
)

selected_category = st.selectbox(
    "Select a product category",
    categories
)

if selected_category == "All Categories":
    filtered_df = df.copy()
else:
    filtered_df = df[df["Primary Category"] == selected_category]

    # Create the scatter plot
fig = px.scatter(
    filtered_df,
    x="sugars_100g",
    y="proteins_100g",
    color="Primary Category",
    hover_data=["product_name"],
    title="Sugar vs Protein by Product Category",
    labels={
        "sugars_100g": "Sugar per 100g (g)",
        "proteins_100g": "Protein per 100g (g)"
    },
    opacity=0.4,
    render_mode="webgl"
)

# Add the opportunity threshold lines
fig.add_vline(x=4.31, line_dash="dash", line_color="red")
fig.add_hline(y=12, line_dash="dash", line_color="green")
# Highlight the nutritional opportunity area

# Shade the high-protein, low-sugar quadrant
fig.add_shape(
    type="rect",
    xref="x",
    yref="y",
    x0=0,
    x1=4.31,
    y0=12,
    y1=100,
    fillcolor="rgba(0, 128, 0, 0.12)",
    line=dict(width=0),
    layer="above"
)

# Keep the full nutrient range visible
fig.update_xaxes(range=[0, 100])
fig.update_yaxes(range=[0, 100])

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Display the key business insight
st.subheader("Key Market Insight")

st.info(
    "Based on the data, the opportunity for the client's "
    "healthy-snacking line is within the Snacks category, "
    "targeting products with more than 12g of protein and "
    "less than 4.31g of sugar per 100g. "
    "Only 6,190 of 55,836 snack products (11.09%) "
    "meet these criteria."
)
# Create a summary of opportunity products by category
category_summary = df.groupby("Primary Category").agg(
    Total_Products=("product_name", "count"),
    Opportunity_Products=("Opportunity", "sum")
).reset_index()

# Arrange categories from highest to lowest
category_summary = category_summary.sort_values(
    "Opportunity_Products",
    ascending=False
)


# Create the bar chart to show the n8umber of qualifying products.
fig_bar = px.bar(
    category_summary,
    x="Primary Category",
    y="Opportunity_Products",
    title="Opportunity Products by Category",
    labels={
        "Primary Category": "Product Category",
        "Opportunity_Products": "Number of Opportunity Products"
    },
    text="Opportunity_Products"
)

# Display the chart
st.subheader("Opportunity Products Across Categories")
st.plotly_chart(fig_bar, use_container_width=True)