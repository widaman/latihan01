import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

st.tittle("Data visualization")

# Genarate some data
x = np.lisaspace(0, 10, 100)
y = np.sin(x)
# Plot data
fig, ax = plt.subplots()
ax.plot(x, y)
# Display the plot
st..pyplot(fig)
