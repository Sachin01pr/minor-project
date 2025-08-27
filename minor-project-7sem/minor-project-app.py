import streamlit as st
import pandas as pd
from joblib import load

model = load(r'C:\Users\mayan\OneDrive\Documents\git-projects\minor-project\minor-project-7sem\attrition_model.pkl')
data = pd.read_csv(r'C:\Users\mayan\OneDrive\Documents\git-projects\minor-project\minor-project-7sem\hr_manages.csv')

results = {}
for cols in data.columns:
    if data[cols].nunique()< 10:
        list = data[cols].unique().tolist()
        name_of_input = data[cols].name 
        name_of_input = st.selectbox(f"select {name_of_input}" , list)
        results[cols] = name_of_input

st.dataframe(pd.DataFrame([results]))
        
"""

st.title("HR Attrition Prediction")

excepted_features = ['age', 'businesstravel', 'dailyrate', 'department', 'distancefromhome',
       'education', 'educationfield', 'environmentsatisfaction', 'gender',
       'hourlyrate', 'jobinvolvement', 'joblevel', 'jobrole',
       'jobsatisfaction', 'maritalstatus', 'monthlyincome', 'monthlyrate',
       'numcompaniesworked', 'overtime', 'percentsalaryhike',
       'performancerating', 'relationshipsatisfaction', 'stockoptionlevel',
       'totalworkingyears', 'trainingtimeslastyear', 'worklifebalance',
       'yearsatcompany', 'yearsincurrentrole', 'yearssincelastpromotion',
       'yearswithcurrmanager']

age = st.slider('Age' , 18 , 60 , 25)
gender = st.selectbox(["Female" , "Male"] ,"Enter gender: ")
maritalstatus = st.selectbox(["Divorced" , "Married" , "Single"] ,"Enter marital status: ")
department = st.selectbox(["Human Resources" , "Research & Development" , "Sales"] ,"Enter department: ")
overtime = st.selectbox(["No" , "Yes"] , "Does overtime:")
businesstravel = st.selectbox(["Non-Travel" , "Travel_Frequently" , "Travel_Rarely"] , "Business travel frequency:")
"""