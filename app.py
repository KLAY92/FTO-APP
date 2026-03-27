# PC에서 작성하는 app.py
import streamlit as st
import requests

st.title("🛡️ FTO 자동 분석 시스템")
uploaded_file = st.file_uploader("특허 명세서를 업로드하세요", type=['pdf', 'txt'])

# Colab에서 출력된 URL을 여기에 복사
API_URL = "https://[ngrok에서_생성된_임시주소].ngrok-free.app/run_fto"

if st.button("분석 시작") and uploaded_file:
    with st.spinner("Colab에서 FTO 분석 중입니다..."):
        files = {"patent_file": (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post(API_URL, files=files)
        
        if response.status_code == 200:
            st.success("분석 완료!")
            st.json(response.json())
        else:
            st.error("API 통신 에러")

