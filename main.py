import streamlit as st
import numpy as np
from scipy.stats import norm, poisson, expon

# Setup
st.title("Distribution Visualiser")
st.write("Choose a distribution and adjust the parameters!")

# Sidebar
dist_choice = st.sidebar.selectbox("Select Distribution", ("Normal", "Poisson", "Exponential"))

# Container for parameters based on distribution chosen

if dist_choice == "Normal":
    st.sidebar.write("## Normal Distribution Parameters")
    mean = st.sidebar.slider("Mean (μ)", -10.0, 10.0, 0.0)
    std_dev = st.sidebar.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0)
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = norm.pdf(x, mean, std_dev)
    st.write(f"### Normal distribution with μ={mean} and σ={std_dev}")