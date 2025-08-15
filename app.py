import streamlit as st
import pandas as pd

st.title('UV + Streamlit アプリ')
st.write('このアプリは、UVで作成した仮想環境で動いています。')

df = pd.DataFrame({
    '列1': [1, 2, 3],
    '列2': [10, 20, 30]
})

st.dataframe(df)