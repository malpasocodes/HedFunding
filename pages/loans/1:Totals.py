import streamlit as st
import pandas as pd

# Form to Show Institutions with Most Pell Grant Money

def show():
    st.markdown("### Insitutions Receiving the Most Loan Dollars (Sorted)")
    # Load data
    df = pd.read_csv('data/loan_summary.csv')

    with st.form("top_institutions"):
        st.write("Institutions Receiving the Most Loan Dollars")
        top_n = st.slider('Select number of institutions: ', 1, 50, 5)
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        top_institutions = df.nlargest(top_n, 'Millions$')[['Institution','Control', 'Billions$']]
        st.write(top_institutions)
    