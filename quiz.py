import streamlit as st

st.title("Quiz App")
st.write("이 앱은 간단한 퀴즈를 제공합니다. 아래 질문에 답해주세요!")


question1 = "다음 중 박현준이 담당하는 세션은?"
options = ["기타", "베이스", "키보드", "드럼"]
answer1 = st.radio("질문: " + question1, options)

submit1 = st.button("객관식 제출")
if submit1:
    if answer1 == "드럼":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 다시 시도해보세요.")

st.title("주관식 퀴즈")

question2 = "노래 '시퍼런봄'을 부른 밴드의 이름은?"
correct_answer2 = "쏜애플"
user_input = st.text_input(question2)

submit2 = st.button("주관식 제출")
if submit2:
    if user_input.strip() == correct_answer2:
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 다시 시도해보세요.")