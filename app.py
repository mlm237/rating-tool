import streamlit as st

st.title("AtCoder レーティング計算")
name = st.text_input("名前を入れてください")
if name:
    st.write(f"こんにちは、{name}さん")