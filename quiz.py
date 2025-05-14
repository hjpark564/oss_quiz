import streamlit as st

# 제목
st.title("Quiz App")

# 설명
st.write("이 앱은 간단한 퀴즈를 제공합니다. 아래 질문에 답해주세요!")

# 질문
question = "파이썬의 창시자는 누구일까요?"
options = ["Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg"]

# 선택지
answer = st.radio("질문: " + question, options)

# 제출 버튼
if st.button("제출"):
    if answer == "Guido van Rossum":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 다시 시도해보세요.")