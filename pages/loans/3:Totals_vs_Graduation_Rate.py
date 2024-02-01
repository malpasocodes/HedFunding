import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def show():
    # Load data
    df = pd.read_csv('data/loan_summary.csv')
    df['GradRate'] = df['GradRate']/100



    with st.form("plotly_plot"):
        st.write("Scatter Plot")
        plot_n = st.slider('Select number of institutions to plot', 1, 1000, 10)
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            df_inst = df.nlargest(plot_n, 'Millions$')[['Institution', 'Control', 'Billions$', 'GradRate']]
            
            # Create a scatter plot with Plotly
            fig = px.scatter(df_inst, x='Billions$', y='GradRate', color='Control', hover_data=['Institution'])

            # Add a horizontal red line at y=0.5
            fig.add_hline(y=0.25, line_width=3, line_dash="dash", line_color="red")
            
            # Show the plot in Streamlit
            st.plotly_chart(fig)