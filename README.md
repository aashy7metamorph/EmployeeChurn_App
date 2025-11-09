#  Employee Churn Prediction App 

 This project is a **predictive ML solution** designed to estimate whether an employee is likely to churn from a company.  

Built by: **Aisha Memon **

---

## 🧩 Project Overview

Employee churn is a critical metric for companies. High churn can lead to **loss of talent, productivity, and revenue**.  

This project demonstrates how **Machine Learning (ML) pipelines** and a **Streamlit app** can help managers **predict churn** and make informed decisions.  

---

## 🔍 What the App Does

1. **Predicts Employee Churn**  
   - Users input employee data (demographics, experience, payment tier, etc.).
   - The model predicts if the employee is **likely to leave**.   

2. **Interactive Streamlit Interface**  
   - Friendly UI with **categorical and numerical input fields**.  
   - Real-time predictions with a **styled prediction box**.  

---

## 🛠️ How It Was Built

1. **Data Loading & Exploration**  
   - Employee dataset was loaded into a **Jupyter Notebook**.  
   - Identified **categorical** and **numerical features**.  

2. **Random Forest Classifier** 🌲  
   - Chosen for its **high accuracy, robustness, and interpretability**.  
   - Handles mixed data types and captures **feature interactions**.  

3. **Pipeline Creation** ⚡  
   - **Preprocessing + Model** combined into a pipeline.  
   - Ensures **consistent, reusable, and production-ready workflow**.  
   - Makes it easy to apply the same steps for any new data.  

4. **Pickle & Schema Export** 📦  
   - `pipeline.pkl` stores the trained pipeline.  
   - `features_dict.pkl` defines **feature schema** for inputs.  

5. **Streamlit App Integration** 🌷  
   - Loads pipeline and schema.  
   - Provides **interactive UI** for users.  
   - Outputs predictions in a **visually appealing, girly pastel theme**.  

---

## 🎨 Features & Design Highlights

- **Interactive Inputs:** Categorical dropdowns, numerical number inputs.  
- **Prediction Output:** Gradient-colored boxes with emojis for clarity.  
- **Pastel Theme:** Soft lilacs, pinks, and lavender for a pleasing UI.  
- **Tabs:** Separate sections for **Prediction**, **Data Info**, and **Model Info**.  
- **Responsive Layout:** Works well on different screen sizes.  

---

## 🧠 Learning Outcome

Through this project, you will learn:

- How to create **ML pipelines for real-world tasks**.  
- How to use **Random Forests** effectively.  
- How to deploy **interactive apps with Streamlit**.  
- How to **combine ML + UX design** for end-user adoption.  

---

## 🚀 How to Run the App

1. Clone this repository:

```bash
git clone https://github.com/aashy7metamorph/EmployeeChurn_App.git
cd Churn_virtual
