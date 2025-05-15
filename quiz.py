import streamlit as st


st.title("Quiz App")

st.write("이 앱은 간단한 퀴즈를 제공합니다. 아래 질문에 답해주세요!")


question = "다음 중 박현준이 담당하는 세션은?"
options = ["기타", "베이스", "키보드", "드럼"]

answer = st.radio("질문: " + question, options)

if st.button("제출"):
    if answer == "드럼":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 다시 시도해보세요.")



