import streamlit as st
import pandas as pd

# Form to Show Institutions with Most Pell Grant Money
def show():
     
    # Load data
    df = pd.read_csv('data/pell_summary.csv')

    with st.form("top_institutions"):
        st.write("Institutions Receiving the Most Pell Grant Money")
        top_n = st.slider('Select number of institutions', 1, 20, 5)
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        top_institutions = df.nlargest(top_n, 'PellM$')[['Institution','Control', 'PellB$']]
        st.write(top_institutions)
    