import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import matplotlib.pyplot as plt

st.header('st.write')

st.header('text')
st.markdown("test dla :red[kolorowania]")

st.write(123)
df = pd.DataFrame([[2, 3], [4, 5]], columns=['q', 's'])
st.write('it\'s dataframe', df)

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

d = alt.Chart(df).mark_point().encode(x='q', y='s')
st.write(d)


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig

new = arr.T
new[:10]
if not st.button('Say hello'):
    st.write('Goodbye')
else:
    st.write('Why hello there')
