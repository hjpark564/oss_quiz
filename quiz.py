import streamlit as st


st.title("Quiz App")

st.write("이 앱은 간단한 퀴즈를 제공합니다. 아래 질문에 답해주세요!")


question1 = "다음 중 박현준이 담당하는 세션은?"
options = ["기타", "베이스", "키보드", "드럼"]

answer = st.radio("질문: " + question1, options)

if st.button("제출"):
    if answer == "드럼":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 다시 시도해보세요.")

st.title("주관식 퀴즈")

question2 = "노래 '시퍼런봄'을 부른 밴드의 이름은?"
ans = "쏜애플"

user_input = st.text_input(question2)

if st.button("제출"):
    if user_input.strip().lower() == answer:
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 다시 시도해보세요.")