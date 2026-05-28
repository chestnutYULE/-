import streamlit as st
import random

# 저녁 메뉴 리스트
dinner_list = [
    "치킨",
    "피자",
    "햄버거",
    "귀찮다 이런거 시키지마라",
    "삼겹살",
    "봉구스밥버거",
    "떡볶이",
    "굶어",
    "국밥",
    "아무거나 먹어"
]

# 제목
st.title("🍽️ 저녁 메뉴 추천 앱")

st.write("버튼을 누르면 오늘 저녁 메뉴를 추천해드립니다!")

# 버튼
if st.button("추천 받기"):
    menu = random.choice(dinner_list)
    st.success(f"오늘 저녁은 👉 {menu}")
