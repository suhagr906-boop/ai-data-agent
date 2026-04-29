# 📊 Data Analysis Agent (Streamlit + AI)

An interactive Streamlit web application for quick exploratory data analysis and AI-powered insights on your datasets.

It allows you to:
- Upload CSV/TSV files
- View dataset previews
- Generate statistical summaries
- Visualize distributions
- Ask natural language questions about your data using OpenAI

---

## 🚀 Features

### 📁 Data Upload
- Supports `.csv` and `.tsv` files
- Automatically falls back to `Dataset_dummy.tsv` if no file is uploaded

### 👀 Data Preview
- Displays first 100 rows of the dataset in a clean table

### 📊 Summary Statistics
- Uses pandas describe() for quick statistical overview

### 📈 Visualizations
- Select numeric columns
- Generates histograms using seaborn and matplotlib

### 🤖 AI Data Assistant
- Ask natural language questions about your dataset
- Uses OpenAI GPT model (gpt-4o-mini)
- Sends a sample of your data + question for context-aware answers

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- OpenAI API

---

## 📦 Installation

### 1. Clone the repository
git clone https://github.com/your-username/data-analysis-agent.git
cd data-analysis-agent

### 2. Install dependencies
pip install -r requirements.txt

If requirements.txt is not available:
pip install streamlit pandas matplotlib seaborn openai

---

## 🔑 OpenAI API Setup

This app requires an OpenAI API key for the Ask AI feature.

### Option 1: Streamlit Secrets (Recommended)
Create this file:
.streamlit/secrets.toml

Add:
OPENAI_API_KEY = "your-api-key-here"

---

### Option 2: Environment Variable
export OPENAI_API_KEY="your-api-key-here"

---

## ▶️ Run the App

streamlit run app.py

---

## 📂 Project Structure

data-analysis-agent/
│
├── app.py                  # Main Streamlit application
├── Dataset_dummy.tsv       # Default dataset (optional)
├── README.md               # Project documentation
└── .streamlit/
    └── secrets.toml        # API key (not committed)

---

## ⚠️ Notes

- The AI feature uses only a small sample (first 5 rows) of the dataset
- Best suited for structured tabular data (CSV/TSV)
- Large datasets are not fully sent to the model

---

## 💡 Future Improvements

- Add scatter plots and correlation heatmaps
- Support multiple file uploads
- Export analysis reports (PDF/Excel)
- Improve AI agent with full dataset context
- Add automatic data cleaning suggestions

---

## 🧑‍💻 Author

Built with ❤️ using Streamlit and OpenAI
