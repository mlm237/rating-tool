import streamlit as st
from rating import calc_rating, needed_perf

st.title("AtCoder レーティング計算")

default = "112, 485, 478, 703, 921, 994, 553, 1102, 992, 1123, 798, 1163, 1130, 508, 1030, 1214, 1045, 1097, 1219, 1463, 1067, 959, 1044, 1209, 1315, 1023, 1005, 1351, 1475"
text = st.text_area("過去のパフォーマンス（古い順。カンマか改行で区切る）", default)
target = st.number_input("目標レーティング", value=1200, step=100)

try:
    perfs = [float(x) for x in text.replace(",", " ").replace("、", " ").split()]
except ValueError:
    st.error("数字をカンマか改行で区切って入力してください")
    st.stop()
if not perfs:
    st.info("パフォーマンスを入力してください")
    st.stop()

current = calc_rating(perfs)
st.metric("現在のレーティング", f"{current:.0f}")

if current >= target:
    st.success("すでに目標に到達しています")
else:
    rows = [{"今後の参加回数": n, "必要な平均パフォ": round(needed_perf(perfs, target, n))} for n in [1, 2, 3, 5, 8, 10]]
    st.dataframe(rows, hide_index=True)