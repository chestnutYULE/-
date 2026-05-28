import streamlit as st
import random

# 저녁 메뉴 리스트
dinner_list = [
    "먹긴 뭘 먹어 살이나 빼",
    "굶으라니까",
    "뚱뚱한 니 배?",
    "귀찮다 이런거 시키지마라",
    "너 닮은 삼겹살",
    "봉구스밥버거",
    "먹지마",
    "먹지말라고",
    "잠이나 자라",
    "아무거나 먹어"
]

# 제목
st.title("🍽️ 저녁 메뉴 추천 앱")

st.write("버튼을 누르면 오늘 저녁 메뉴를 추천해드립니다!")

# 버튼
if st.button("추천 받기"):
    menu = random.choice(dinner_list)
    st.success(f"오늘 저녁은 👉 {menu}")
