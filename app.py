import streamlit as st
import pandas as pd

def simple_fto_analysis(keyword):
    return {
        "검색 키워드": keyword,
        "결과": "FTO 분석 준비 완료 (다음 단계에서 실제 분석 연결)"
    }

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

            # 🔥 여기 핵심 변경
            result = simple_fto_analysis(keyword)

        st.success("분석 완료!")
        st.write(result)
