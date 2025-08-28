import streamlit as st
import pandas as pd
from joblib import load

model = load(r'C:\Users\mayan\OneDrive\Documents\git-projects\minor-project\minor-project-7sem\attrition_model.pkl')
data = pd.read_csv(r'C:\Users\mayan\OneDrive\Documents\git-projects\minor-project\minor-project-7sem\hr_manages.csv')

personal = ["age","gender","maritalstatus","education","educationfield","distancefromhome","numcompaniesworked"]


job_related = ["businesstravel", "department","jobrole","joblevel","monthlyincome","monthlyrate","hourlyrate",
               "dailyrate","overtime","stockoptionlevel","percentsalaryhike","performancerating","yearsatcompany"
               ,"yearsincurrentrole","yearssincelastpromotion","yearswithcurrmanager","totalworkingyears"]

satisfaction = [ "environmentsatisfaction", "jobsatisfaction", "relationshipsatisfaction", "worklifebalance", "trainingtimeslastyear", "jobinvolvement"]
st.title("Employee Details")
st.sidebar.subheader("Please enter the following details:")
perinfo = {}
for main_col in [personal , job_related , satisfaction]:
    st.sidebar.subheader(f"Enter {main_col[0].capitalize()} related details:")
    for col in main_col:
        if data[col].nunique()< 10 :
            list = data[col].unique().tolist()
            name_of_input = data[col].name
            value_of_input = st.sidebar.selectbox(f"select {name_of_input}" , list)
            perinfo[name_of_input] = value_of_input
        elif data[col].nunique()>= 10 and data[col].dtype == 'int64':
            min_value = int(data[col].min())
            max_value = int(data[col].max())
            name_of_input = str(data[col].name)
            value_of_input = st.slider(f"select {name_of_input}" , min_value , max_value , int(data[col].mean()))
            perinfo[name_of_input] = value_of_input
        elif data[col].nunique()>= 10 and data[col].dtype == 'object':
            name_of_input = data[col].name
            value_of_input = st.selectbox(f"select {name_of_input}" , data[col].unique().tolist())
            perinfo[name_of_input] = value_of_input
st.subheader("Employee details you entered:")
st.dataframe(pd.DataFrame(perinfo , index=[0]))
print(perinfo)
input_df = pd.DataFrame([perinfo])
if st.button("Predict Attrition"):
    result = model.predict(input_df)[0]
    if result == 1:
        st.error("The employee is likely to leave the company.")
    else:
        st.success("The employee is likely to stay with the company.")