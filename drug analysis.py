import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Medicine Dashboard", layout="wide")

st.title("💊 Medicine Information Dashboard")
st.markdown("Enter a medicine name to view its side effects and uses.")

# ------------------------------------------------------
# 1. USER INPUT
# ------------------------------------------------------
medicine_input = st.text_input("Enter medicine name:")

# ------------------------------------------------------
# 2. SIMPLE BUILT-IN DATA (you can expand this dictionary)
# ------------------------------------------------------
# Example dictionary for demo purposes
medicine_data = {
    "paracetamol": {
        "side_effects": "Nausea, rash, liver damage (rare with overdose)",
        "uses": "Pain relief, fever reduction"
    },
    "ibuprofen": {
        "side_effects": "Stomach upset, dizziness, kidney issues (long-term use)",
        "uses": "Pain relief, inflammation reduction, fever reduction"
    },
    "amoxicillin": {
        "side_effects": "Diarrhea, nausea, allergic reactions",
        "uses": "Treats bacterial infections"
    }
}

# ------------------------------------------------------
# 3. DISPLAY RESULTS
# ------------------------------------------------------
if medicine_input:
    key = medicine_input.strip().lower()
    if key in medicine_data:
        st.subheader(f"Results for: {medicine_input.title()}")
        st.info(f"**Side Effects:** {medicine_data[key]['side_effects']}")
        st.success(f"**Uses:** {medicine_data[key]['uses']}")
    else:
        st.warning("No information found for that medicine. Try another name.")
