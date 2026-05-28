import streamlit as st
import random

# 저녁 메뉴 리스트
dinner_list = [
    "치킨",
    "피자",
    "햄버거",
    "김치찌개",
    "삼겹살",
    "초밥",
    "떡볶이",
    "파스타",
    "국밥",
    "쌀국수"
]

# 제목
st.title("🍽️ 저녁 메뉴 추천 앱")

st.write("버튼을 누르면 오늘 저녁 메뉴를 추천해드립니다!")

# 버튼
if st.button("추천 받기"):
    menu = random.choice(dinner_list)
    st.success(f"오늘 저녁은 👉 {menu}")
