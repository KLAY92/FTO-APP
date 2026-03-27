import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🚀 FTO 자동 분석 시스템")

# 사이드바
st.sidebar.header("🔧 분석 설정")

keyword = st.sidebar.text_input("기술 키워드", "배터리 열관리 시스템")
top_n = st.sidebar.slider("특허 개수", 5, 50, 20)

# 파일 업로드
st.subheader("📄 문서 업로드")

patent_file = st.file_uploader("특허 명세서", type=["pdf", "txt"])

# 실행 버튼
if st.button("🔥 FTO 분석 실행"):

    if patent_file is None:
        st.error("특허 명세서를 업로드하세요")
    else:
        with st.spinner("분석 진행 중..."):

            data = {
                "특허번호": ["KR123", "KR456", "KR789"],
                "위험도": ["HIGH", "MEDIUM", "LOW"],
                "유사도": [85, 60, 30]
            }

            df = pd.DataFrame(data)

        st.success("분석 완료!")

        st.dataframe(df)
        st.bar_chart(df["유사도"])
