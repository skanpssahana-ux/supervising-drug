import streamlit as st

# Page Configuration
st.set_page_config(page_title="Medicine Dashboard", layout="wide")

st.title("💊 Medicine Information Dashboard")
st.markdown("Enter a medicine name to view its side effects and uses.")

# ------------------------------------------------------
# 1. Built-in Medicine Data
# ------------------------------------------------------
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
    },
    "cetirizine": {
        "side_effects": "Drowsiness, dry mouth, fatigue",
        "uses": "Relief from allergy symptoms like sneezing, runny nose, itching"
    },
    "omeprazole": {
        "side_effects": "Headache, abdominal pain, diarrhea",
        "uses": "Reduces stomach acid, treats GERD and ulcers"
    }
}

# ------------------------------------------------------
# 2. User Input
# ------------------------------------------------------
medicine_input = st.text_input("Enter medicine name:")

# ------------------------------------------------------
# 3. Display Results
# ------------------------------------------------------
if medicine_input:
    key = medicine_input.strip().lower()
    if key in medicine_data:
        st.subheader(f"Results for: {medicine_input.title()}")
        st.info(f"**Side Effects:** {medicine_data[key]['side_effects']}")
        st.success(f"**Uses:** {medicine_data[key]['uses']}")
    else:
        st.warning("No information found for that medicine. Try another name.")
