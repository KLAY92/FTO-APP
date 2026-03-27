import streamlit as st
import requests

st.title("🚀 FTO 분석 시스템")

# ==============================
# 입력 영역
# ==============================
keyword = st.text_input("🔍 검색 키워드 입력")

patent_text = st.text_area("📄 특허 명세서 입력", height=300)

# ==============================
# 실행 버튼
# ==============================
if st.button("🔥 FTO 분석 실행"):

    if not keyword:
        st.error("키워드를 입력하세요")
    elif not patent_text:
        st.error("특허 명세서를 입력하세요")
    else:
        with st.spinner("분석 진행 중..."):

            # 🔥 여기다 넣는거다
            response = requests.post(
                "https://xxxx.ngrok-free.app/fto",  # 👈 Colab에서 나온 주소
                json={
                    "keyword": keyword,
                    "patent_text": patent_text
                }
            )

            # ==============================
            # 디버깅 (중요🔥)
            # ==============================
            st.write("상태코드:", response.status_code)
            st.write("응답내용:", response.text)

            # ==============================
            # 결과 출력
            # ==============================
            try:
                result = response.json()

                st.success("분석 완료!")

                st.subheader("📊 요약 결과")
                st.write(result["summary"])

                st.subheader("📌 상세 결과")
                for r in result["results"]:
                    st.write(r)

            except:
                st.error("❌ JSON 변환 실패")
