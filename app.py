import streamlit as st
import requests

# 페이지 기본 설정
st.set_page_config(page_title="FTO 자동 분석 시스템", page_icon="🛡️", layout="centered")

st.title("🛡️ FTO 자동 분석 시스템 (프라이빗 UI)")
st.markdown("---")

# 🌟 아까 Colab에서 뜬 URL을 여기에 복사해 줍니다. (매번 바뀌므로 입력창으로 뺐습니다)
API_URL = st.text_input(
    "🔗 Colab 백엔드 URL을 입력하세요 (끝에 /run_fto 추가)", 
    value="https://unslashed-inflictive-eusebia.ngrok-free.dev/run_fto"
)

st.subheader("📄 분석 문서 업로드")
upload_patent = st.file_uploader("1️⃣ 특허 명세서 (필수 첨부)", type=['pdf', 'txt'])

if st.button("🚀 분석 시작 (서버 전송)", type="primary"):
    if not upload_patent:
        st.warning("🚨 특허 명세서를 먼저 업로드해주세요!")
    else:
        with st.spinner("Colab 서버로 파일을 전송하고 응답을 기다리는 중입니다..."):
            try:
                # 1. 전송할 파일 세팅
                files = {
                    "patent_file": (upload_patent.name, upload_patent.getvalue(), upload_patent.type)
                }
                
                # 2. API 백엔드(Colab)로 POST 요청 쏘기
                response = requests.post(API_URL, files=files)
                
                # 3. 응답 결과 처리
                if response.status_code == 200:
                    st.success("✅ 서버 통신 및 처리 성공!")
                    st.json(response.json()) # 백엔드에서 온 JSON 띄워주기
                else:
                    st.error(f"🚨 서버 에러 발생: HTTP {response.status_code}")
            except Exception as e:
                st.error(f"🚨 통신 오류가 발생했습니다: {e}")

