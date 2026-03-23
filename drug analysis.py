import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Medicine Dashboard", layout="wide")

st.title("💊 Medicine Information Dashboard")
st.markdown("Search for a medicine to view its side effects and uses.")

# ------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")
    st.write("Available columns:", df.columns.tolist())

    # Normalize column names (lowercase, strip spaces)
    df.columns = df.columns.str.strip().str.lower()

    # ------------------------------------------------------
    # 2. USER INPUT
    # ------------------------------------------------------
    medicine_input = st.text_input("Enter medicine name:")

    if medicine_input:
        # Case-insensitive search
        matches = df[df["drug_name"].str.lower() == medicine_input.lower()]

        if not matches.empty:
            st.subheader(f"Results for: {medicine_input.title()}")

            for _, row in matches.iterrows():
                st.info(f"**Side Effects:** {row['side_effects']}")
                st.success(f"**Uses:** {row['uses']}")
        else:
            st.warning("No matching medicine found in dataset. Try another name.")
else:
    st.info("Please upload a CSV file to begin.")
