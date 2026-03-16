import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Page Configuration
st.set_page_config(page_title="Drug Side-Effect Dashboard", layout="wide")

st.title("💊 Drug Side-Effect Analysis Dashboard")
st.markdown("This application analyzes drug datasets for common side effects, medical conditions, and safety guidance.")

# ------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------
# Added a file uploader so you don't have to hardcode the path
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")
    
    # Create Tabs for Organization
    tab1, tab2, tab3 = st.tabs(["📊 Data Analysis", "📈 Visualizations", "🛡️ Safety Guidance"])

    with tab1:
        st.header("Top Side Effects & Analysis")
        
        # side_effects analysis
        if "side_effects" in df.columns:
            df["side_effects"] = df["side_effects"].astype(str).fillna("")
            
            all_effects = []
            for row in df["side_effects"]:
                effects = [x.strip().lower() for x in row.split(",") if x.strip()]
                all_effects.extend(effects)
            
            effect_counts = Counter(all_effects)
            top_5_effects = effect_counts.most_common(5)

            # Display as Metrics
            cols = st.columns(5)
            for i, (effect, count) in enumerate(top_5_effects):
                cols[i].metric(label=effect.title(), value=count)
        else:
            st.error("Column 'side_effects' not found in dataset.")

        st.divider()

        # Severity analysis
        if "drug" in df.columns and "severity" in df.columns:
            st.subheader("Top 5 Drugs by Average Severity")
            severity_scores = df.groupby("drug")["severity"].mean().sort_values(ascending=False).head(5)
            st.table(severity_scores)
        else:
            st.info("Severity analysis unavailable: 'drug' or 'severity' columns missing.")

    with tab2:
        st.header("Data Visualizations")
        
        col_left, col_right = st.columns(2)

        # 1. BAR CHART – Most common drugs
        with col_left:
            if 'drug_name' in df.columns:
                st.subheader("Top 10 Most Common Drugs")
                fig1, ax1 = plt.subplots()
                df['drug_name'].value_counts().head(10).plot(kind='bar', ax=ax1)
                ax1.set_ylabel("Count")
                plt.xticks(rotation=45, ha='right')
                st.pyplot(fig1)
            else:
                st.warning("Please ensure 'drug_name' column exists for Bar Chart.")

        # 2. PIE CHART – Medical conditions
        with col_right:
            if 'medical_condition' in df.columns:
                st.subheader("Top 10 Medical Conditions")
                fig2, ax2 = plt.subplots()
                df['medical_condition'].value_counts().head(10).plot(kind='pie', autopct="%1.1f%%", ax=ax2)
                ax2.set_ylabel("") 
                st.pyplot(fig2)
            else:
                st.warning("Please ensure 'medical_condition' column exists for Pie Chart.")

        st.divider()

        # 3. SCATTER PLOT – Lengths
        if 'drug_name' in df.columns and 'side_effects' in df.columns:
            st.subheader("Drug Name Length vs. Side Effects Description Length")
            df["drug_len"] = df["drug_name"].astype(str).apply(len)
            df["side_len"] = df["side_effects"].astype(str).apply(len)
            
            fig3, ax3 = plt.subplots(figsize=(10, 5))
            ax3.scatter(df["drug_len"], df["side_len"], alpha=0.5)
            ax3.set_xlabel("Length of Drug Name")
            ax3.set_ylabel("Length of Side Effects Text")
            st.pyplot(fig3)

    with tab3:
        st.header("General Safety & Prevention")
        
        c1, c2 = st.columns(2)
        with c1:
            st.info("### General Safety Practices")
            st.markdown("""
            - Keep track of symptoms and when they appear.
            - Read medication instructions carefully.
            - Store medications safely and properly.
            - Report unusual symptoms to a professional.
            - Avoid mixing medications unless confirmed safe.
            """)
        
        with c2:
            st.info("### Side Effect Guidance")
            st.markdown("""
            - **Tiredness:** Rest can help.
            - **Stomach Discomfort:** Stay hydrated and eat consistently.
            - **Headaches:** Reduce screen time or rest in a quiet place.
            - **Dizziness:** Sit down immediately to prevent falls.
            """)

else:
    st.info("Please upload a CSV file to begin the analysis.")
