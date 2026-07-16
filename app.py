
import streamlit as st
import pandas as pd

st.title("학적 등록")

if "student_list" not in st.session_state:
    st.session_state.student_list = []

student_ID = st.text_input('학번을 입력하세요.')
name = st.text_input('이름을 입력하세요.')
major = st.text_input('학과를 입력하세요.')

if st.button("등록"):
    if student_ID and name and major:
        new_data = {
            "학번": student_ID,
            "이름": name,
            "전공": major
        }
        st.session_state.student_list.append(new_data)
        st.success("학적이 추가되었습니다!")
    else:
        st.warning("학번, 이름, 학과를 모두 입력해주세요.")

if st.session_state.student_list:
    st.subheader("전체 학적 목록")
    df = pd.DataFrame(st.session_state.student_list)
    st.table(df)

