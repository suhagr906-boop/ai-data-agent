import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openai import OpenAI
import os

# CONFIG
st.set_page_config(page_title="Data Agent Dashboard", layout="wide")
st.title("📊 Data Analysis Agent")

# REPRODUCIBILITY: Load default file if none is uploaded
uploaded_file = st.file_uploader("Upload your dataset (CSV/TSV)", type=["csv", "tsv"])

if uploaded_file is not None:
    sep = "\t" if uploaded_file.name.endswith("tsv") else ","
    df = pd.read_csv(uploaded_file, sep=sep)
elif os.path.exists("Dataset_dummy.tsv"):
    df = pd.read_csv("Dataset_dummy.tsv", sep="\t")
    st.info("Using default dataset: Dataset_dummy.tsv")
else:
    st.error("Dataset not found. Please upload a file.")
    st.stop()

# SIDEBAR
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose Action", ["Preview", "Summary", "Visuals", "Ask AI"])

if option == "Preview":
    st.dataframe(df.head(100))

elif option == "Summary":
    st.write(df.describe())

elif option == "Visuals":
    cols = df.select_dtypes(include=['number']).columns.tolist()
    if cols:
        col = st.selectbox("Select Column", cols)
        fig, ax = plt.subplots()
        sns.histplot(df[col], ax=ax)
        st.pyplot(fig)

elif option == "Ask AI":
    q = st.text_input("Ask a question about the data")
    if st.button("Submit") and q:
        try:
            client = OpenAI() # Needs OPENAI_API_KEY in Streamlit Secrets
            prompt = f"Data sample: {df.head(5).to_string()}\nQuestion: {q}"
            resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
            st.write(resp.choices[0].message.content)
        except:
            st.error("Configure OpenAI API Key in Streamlit Settings.")
