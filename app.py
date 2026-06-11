app.py
import streamlit as st
from google import genai
from google.genai import types

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🎬 영화 추천 챗봇",
    page_icon="🎬",
)

st.title("🎬 영화 추천 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반 영화 추천 서비스")

# -----------------------------
# API 키 확인
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error(
        "GEMINI_API_KEY가 설정되지 않았습니다. Streamlit Secrets를 확인하세요."
    )
    st.stop()

# -----------------------------
# Gemini Client
# -----------------------------
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Gemini 클라이언트 생성 실패: {e}")
    st.stop()

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요! 🎬\n\n"
                "좋아하는 영화, 장르, 분위기를 알려주시면 "
                "취향에 맞는 영화를 추천해드릴게요."
            ),
        }
    ]

# -----------------------------
# 이전 대화 표시
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
prompt = st.chat_input("어떤 영화를 추천받고 싶나요?")

if prompt:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("영화를 찾는 중..."):

            try:

                # 대화 이력 구성
                conversation_text = ""

                for msg in st.session_state.messages:
                    role = "사용자" if msg["role"] == "user" else "AI"
                    conversation_text += (
                        f"{role}: {msg['content']}\n"
                    )

                system_prompt = """
당신은 전문 영화 추천가입니다.

규칙:
1. 사용자의 취향을 분석한다.
2. 영화 추천 시 제목, 개봉연도, 추천 이유를 제공한다.
3. 최소 3편 이상 추천한다.
4. 스포일러는 하지 않는다.
5. 답변은 한국어로 작성한다.
6. 영화와 관련 없는 질문도 친절히 답변한다.
"""

                full_prompt = f"""
{system_prompt}

대화 기록:
{conversation_text}

사용자 요청:
{prompt}
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=full_prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.8,
                        max_output_tokens=1000,
                    ),
                )

                answer = response.text

            except Exception as e:
                answer = (
                    "죄송합니다. 응답을 생성하는 중 오류가 발생했습니다.\n\n"
                    f"오류 내용: {str(e)}"
                )

        st.markdown(answer)

    # 응답 저장
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# -----------------------------
# 사이드바
# -----------------------------
with st.sidebar:

    st.header("설정")

    if st.button("대화 초기화"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "안녕하세요! 🎬\n\n"
                    "좋아하는 영화나 장르를 알려주세요."
                ),
            }
        ]
        st.rerun()

    st.divider()

    st.markdown(
        """
### 사용 예시

- 액션 영화 추천해줘
- 인터스텔라 같은 영화 알려줘
- 넷플릭스에서 볼만한 스릴러 추천
- 울고 싶을 때 볼 영화 추천
- 크리스토퍼 놀란 작품 추천
"""
    )
