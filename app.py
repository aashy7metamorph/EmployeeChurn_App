import streamlit as st
import pandas as pd
from joblib import load
import dill

# It opens the pkl file as context. 
with open('pipeline.pkl', 'rb') as file:
    model = dill.load(file)

my_feature_dict = load('my_feature_dict.pkl')

st.set_page_config(
    page_title="🌸  Employee Churn Predictor 🌸",
    page_icon="💜 ",
    layout="centered",
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fff0f5 0%, #f8f0ff 100%);
}
h1, h2, h3, h4 {
    color: #9b59b6;
    text-shadow: 1px 1px 1px #ffffff;
    font-family: 'Trebuchet MS', sans-serif;
}
p, label {
    color: #333333;
}
.stButton>button {
    background-color: #d8aee1;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 0.7em 1.5em;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #c38fcf;
    color: #222;
}
div[data-baseweb="select"] span {
    color: #333333 !important;
}
.stNumberInput input {
    background-color: #f5e6fa;
    color: #333333;
    border-radius: 6px;
    padding: 0.5em;
}
hr {
    border: 1px solid #d8aee1;
}
footer {
    color: #9b59b6;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fff0f5 0%, #f8f0ff 100%);
    border: 5px solid #d8aee1;
    border-radius: 15px;
    box-shadow: 0px 8px 20px rgba(155, 89, 182, 0.3);
    padding: 20px;
    margin-top: 20px;
}
header {
    background-color: #fff0f5;
    border-bottom: 3px solid #d8aee1;
    border-radius: 15px 15px 0 0;
}
h1, h2, h3, h4 {
    color: #9b59b6;
    text-shadow: 1px 1px 1px #ffffff;
    font-family: 'Trebuchet MS', sans-serif;
}
.stButton>button {
    background-color: #d8aee1;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 0.7em 1.5em;
}
.stButton>button:hover {
    background-color: #c38fcf;
    color: #222;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌷 About this App")
st.sidebar.info("""
Predict whether an **employee is likely to churn**.

Built by **Aisha Memon 💜**  
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Quick Links")
st.sidebar.markdown("[GitHub Repository](https://github.com/)")

tab1, tab2, tab3 = st.tabs(["🔮 Predict Churn", "📘 About Data", "⚙️ Model Info"])

with tab1:
    st.title("🌸 Employee Churn Prediction 🌸")
    st.subheader("Fill in employee details below")

    st.markdown("#### 🎀 Categorical Features")
    categorical_input = my_feature_dict.get('CATEGORICAL')
    categorical_input_vals = {}
    cols = st.columns(2)
    for i, col in enumerate(categorical_input.get('Column Name').values()):
        with cols[i % 2]:
            categorical_input_vals[col] = st.selectbox(
                f"{col}",
                categorical_input.get('Members')[i],
                key=col
            )

    st.markdown("#### 💫 Numerical Features")
    numerical_input = my_feature_dict.get('NUMERICAL')
    numerical_input_vals = {}
    cols2 = st.columns(2)
    for i, col in enumerate(numerical_input.get('Column Name')):
        with cols2[i % 2]:
            numerical_input_vals[col] = st.number_input(
                f"{col}",
                key=col,
                step=1.0
            )

    input_data = dict(list(categorical_input_vals.items()) + list(numerical_input_vals.items()))
    input_data = pd.DataFrame.from_dict(input_data, orient='index').T

    st.markdown("---")
    if st.button("✨ Predict ✨"):
        prediction = model.predict(input_data)[0]
        translation_dict = {"Yes": "⚠️ Expected to Churn", "No": "💜 Likely to Stay"}
        message = translation_dict.get(prediction)

        if prediction == "Yes":
            st.markdown(f'<div style="background-color:#f7c6de; border-radius:10px; padding:1em; text-align:center; font-size:1.2em;">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="background-color:#e9d7f0; border-radius:10px; padding:1em; text-align:center; font-size:1.2em;">{message}</div>', unsafe_allow_html=True)

        with st.expander("🔍 View Input Summary"):
            st.dataframe(input_data)
    else:
        st.info("Fill all fields and click *Predict*.")

with tab2:
    st.header("📘 About the Dataset")
    st.markdown("""
This dataset contains employee details such as:

- **Demographics:** Gender, City, Education  
- **Professional info:** Joining Year, Experience  
- **Behavioral factors:** Ever Benched, Payment Tier  

Goal: Predict if an employee will **leave the company (churn)**.
""")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.markdown("---")
    st.caption("Data used in model training. Confidential and anonymized.")

with tab3:
    st.header("⚙️ Model Information")
    st.markdown("""
**Model Type:** ML Pipeline  
**Libraries:** scikit-learn, pandas, dill  
**Features:** Categorical + Numerical preprocessing  
**Target:** Leave / Churn
""")
    with st.expander("View Features"):
        st.write(model.feature_names_in_ if hasattr(model, 'feature_names_in_') else "Feature names not stored.")
    st.metric("Model Accuracy", "≈ 93%")
    st.metric("Training Data Size", "~4000+ rows")
    st.markdown("🧠 Reliable predictions powered by Aisha’s ML pipeline.")

st.markdown("---")
st.markdown('<p style="text-align:center; color:#9b59b6 ; font-size:35px">Designed by Aisha🌷 — Streamlit app</p>', unsafe_allow_html=True)

