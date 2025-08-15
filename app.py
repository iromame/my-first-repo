# streamlit_app/app.py
import streamlit as st
import pandas as pd

st.title('Streamlitアプリの新しい機能')
st.write('これはGitHubを更新する練習です。')

# ユーザーからの入力を受け取るテキストボックス
user_input = st.text_input("ここにテキストを入力してください")

# 入力されたテキストを表示
if user_input:
    st.write(f'入力されたテキスト: {user_input}')

df = pd.DataFrame({
    '列1': [1, 2, 3, 4],
    '列2': [10, 20, 30, 40]
})
st.write(df)