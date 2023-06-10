import numpy as np
import altair as alt
import panda as pd
import streamlit as st

st.header ('st.write')
st.write('Hello *world* :sunglasses:')
st.write(1,2,3,4)
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
    })