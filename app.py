import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image
import pickle

model = pickle.load(open('C:/Users/HP/Desktop/SDP Final/logistic_model.pkl','rb'))
def run():
    img1 = Image.open('bank.jpg')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width = False)
    st.title("Bank Loan Prediction Using Machine Learning")

    ##Account no
    account_no = st.text_input('Account Number')

    ##Full name 
    fn = st.text_input('Full Name')

    ##For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func = lambda x:gen_display[x])

    ##For marital status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status",mar_options, format_func = lambda x:mar_display[x])

    ##No of dependents
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",dep_options, format_func = lambda x:dep_display[x])

    #For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func = lambda x:edu_display[x])

    ##For emp status
    emp_display = ('Job','Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func = lambda x:emp_display[x])

    #For property status
    prop_display = ('Rural','Semi-Urban', 'Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area",prop_options, format_func = lambda x:prop_display[x])

    ##For credit score
    cred_display = ('Between 300 to 500','Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score",cred_options, format_func = lambda x:cred_display[x])

    ##Applicant monthly income
    mon_income = st.number_input("Applicant's Monthly Income($)",value = 0)

    ##Co-applicant monthly income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value = 0)

    ##loan amount
    loan_amt = st.number_input("Loan Amount", value = 0)

    ##loan duration
    dur_display = ['2 months', '6 months', '8 months','1 Year', '16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func = lambda x:dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[cred, gen, edu]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i)for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello: "+fn+ " || "
                "Account Number: "+account_no +' || '
                'According to our calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello: "+fn+ " || "
                "Account Number: "+account_no +' || '
                'Congratulations!! You will get the loan from Bank'
            )

run()