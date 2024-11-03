import streamlit as st
import numpy as np
from scipy.stats import norm, poisson, expon
import matplotlib.pyplot as plt

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
    x = np.linspace(-15, 15, 1000)
    y = norm.pdf(x, mean, std_dev)
    st.write(f"### Normal distribution with μ={mean} and σ={std_dev}")
elif dist_choice == "Poisson":
    st.write("## Poisson Distribution Parameters")
    mean = st.sidebar.slider("Lambda(λ)", 1, 20, 5)
    x = np.arange(0, 30)
    y = poisson.pmf(x, mean)
    st.write(f"### Poisson distribution with λ={mean}")
elif dist_choice == "Exponential":
    st.sidebar.write("## Exponential Distribution Parameters")
    rate = st.sidebar.slider("Rate (λ)", 0.1, 2.0, 1.0)
    x = np.linspace(0, 10, 1000)
    y = expon.pdf(x, scale=1/rate)
    st.write(f"### Exponential distribution with λ={rate}")

# Plot the distribution
fig, ax = plt.subplots()

if dist_choice in ["Normal", "Exponential"]:
    ax.plot(x, y, label=dist_choice)
    ax.fill_between(x, y, alpha=0.2)
else:
    ax.bar(x, y, label=dist_choice, alpha=0.6)

ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
ax.legend()
st.pyplot(fig)

