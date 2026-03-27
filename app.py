import streamlit as st
import requests

# ==============================
# UI 설정
# ==============================
st.set_page_config(layout="wide")
st.title("🚀 FTO 자동 분석 시스템")

# 사이드바
keyword = st.sidebar.text_input("기술 키워드", "배터리 열관리 시스템")

# 파일 업로드
st.subheader("📄 문서 업로드")
patent_file = st.file_uploader("특허 명세서", type=["pdf", "txt"])

# ==============================
# 분석 버튼
# ==============================
if st.button("🔥 FTO 분석 실행"):

    if patent_file is None:
        st.error("특허 명세서를 업로드하세요")
    else:
        with st.spinner("분석 진행 중..."):

            response = requests.post(
                "https://unslashed-inflictive-eusebia.ngrok-free.dev/fto",   # 🔥 여기 수정
                json={"keyword": keyword},
                headers={
                    "ngrok-skip-browser-warning": "true",
                    "User-Agent": "Mozilla/5.0"
                }
            )

            # 🔥 디버깅 출력
            st.write("상태코드:", response.status_code)
            st.write("응답내용:", response.text)

            try:
                result = response.json()
                st.success("분석 완료!")
                st.write(result)
            except:
                st.error("❌ JSON 변환 실패")
