import webbrowser
import urllib.parse
import pandas as pd
import streamlit as st

st.title("Hierarchical Data Viewer")



df_orig = pd.read_csv("data/employees.csv",header =0).convert_dtypes()


tabs = st.tabs(["source","Graph","Dot-code"])

tabs[0].dataframe(df_orig)

def getGraph(df):
    edges = ""
    for _,row in df.iterrows():

        if not pd.isna(row.iloc[1]):

            edges += f'\t "{row.iloc[1]}" -> "{row.iloc[0]}";\n'
    
    d = f'digraph{{\n{edges}}}'
    return d


cols = list(df_orig.columns)
child = st.sidebar.selectbox("Child Column Name",cols,index = 0)
parent = st.sidebar.selectbox("Parent Column Name",cols,index = 0)
df = df_orig[[child,parent]]

chart = getGraph(df)
tabs[1].graphviz_chart(chart)

        
        
    



url = f'http://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(chart)}'

tabs[2].link_button("Visulize online",url)
tabs[2].code(chart)