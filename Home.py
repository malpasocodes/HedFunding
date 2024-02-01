import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import importlib

groups = {
    'Pell Grant': ['1:Totals','2:Totals_by_Type', '3:Totals_vs_Graduation_Rate'], 
    'Federal Loans': ['1:Totals','2:Totals_by_Type', '3:Totals_vs_Graduation_Rate']
}


st.title('Pell Grants, Federal Loans, Student Outcomes')
st.markdown("""This app is designed to help you explore the relationship between Pell Grants, Federal Loans, and 
            student outcomes at US colleges and universities. It's a work in progress, so please be patient.""")

st.sidebar.title('Navigation')
st.divider()

# Sidebar for selecting group
selected_group = st.sidebar.selectbox("Select a Group", list(groups.keys()))

# Convert the group name to its corresponding folder name
folder_name = "pell" if selected_group == "PellGrant" else "loans"

# Sidebar for selecting page within the group
selected_page = st.sidebar.selectbox("Select a Page", groups[selected_group])

# Dynamically load the selected page from the appropriate subfolder
page = importlib.import_module(f"pages.{folder_name}.{selected_page}")
page.show()  # Assuming each page script has a 'show()' function to run the page





