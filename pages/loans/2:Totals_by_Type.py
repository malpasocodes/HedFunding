import streamlit as st
import pandas as pd


def show():
# Load data
    df = pd.read_csv('data/loan_summary.csv')

    with st.form("institution_type"):
        st.write("Top Institutions by Type")
        control = st.selectbox('Select institution type', df['Control'].unique())
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        top_institutions = df[df['Control'] == control].nlargest(10, 'Millions$')[['Institution','Control', 'Millions$','Billions$','GradRate']]
        st.write(top_institutions)

