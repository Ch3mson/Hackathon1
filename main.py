import streamlit as st
import pandas as pd
import os


st.write("DID I FINALLY FINISH IT????")
dataset1 = pd.read_excel('Ranking_Variables_-_Trade_Area_1_1.xlsx')
print(dataset1)
st.dataframe(dataset1)