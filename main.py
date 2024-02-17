import streamlit as st
import streamlit.components.v1 as components

# Set the page to wide mode
st.set_page_config(layout="wide")

html_file = 'visualizations/aditional_applicants_map.html'

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()
    # Adjust the height as needed, and consider setting width to 100% if suitable
    components.html(html_content, height=2000, scrolling=True)