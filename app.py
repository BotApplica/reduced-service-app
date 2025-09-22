import streamlit as st
from math import floor

# App config
st.set_page_config(page_title="Reduced Service Calculator", page_icon="🚌", layout="wide")

# Force white background with custom CSS
st.markdown(
    """
    <style>
        .stApp {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout for logo + header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7d/Buses_roundel.svg", width=70)
with col2:
    st.markdown("<h1 style='color:red;'>Reduced service calculator</h1>", unsafe_allow_html=True)

st.write("---")

# Input field
total_buses = st.number_input("Enter total number of buses:", min_value=1, step=1)

# Calculation
if total_buses:
    allowed_buses = floor(total_buses * 0.299)
    st.success(f"✅ Maximum buses allowed: **{allowed_buses}** (to stay under 29.9%)")
