import streamlit as st

# Setup
st.title("Distribution Visualiser")
st.write("Choose a distribution and adjust the parameters!")

# Sidebar
dist_choice = st.sidebar.selectbox("Select Distribution", ("Normal", "Poisson", "Exponential"))