import pandas as pd
import streamlit as st
import plotly.graph_objects as go 

df = pd.read_csv("data/employees.csv",header =0).convert_dtypes()

st.dataframe(df)

labels = df[df.columns[0]]
parents = df[df.columns[1]]

print(df.columns[0])
print(df.columns[1])

