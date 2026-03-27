import streamlit as st
import requests
import time

st.set_page_config(page_title="FTO 자동 분석 시스템", page_icon="🛡️", layout="centered")

st.title("🛡️ FTO 자동 분석 시스템 (프라이빗 UI)")
st.markdown("Colab 백엔드와 비동기로 통신하여 대용량 특허(1,000건 이상)를 안전하게 분석합니다.")

API_URL = st.text_input("🔗 Colab 백엔드 URL", value="https://[여기에_ngrok_주소입력].ngrok-free.dev")

upload_patent = st.file_uploader("📄 특허 명세서 업로드 (PDF/TXT)", type=['pdf', 'txt'])

if st.button("🚀 분석 시작 (백그라운드 전송)", type="primary"):
    if not upload_patent:
        st.warning("특허 명세서를 업로드해주세요!")
    else:
        # 1. 파일 접수 (API 호출)
        with st.spinner("서버에 작업을 접수하고 있습니다..."):
            files = {"patent_file": (upload_patent.name, upload_patent.getvalue(), upload_patent.type)}
            res = requests.post(f"{API_URL.rstrip('/')}/start_fto", files=files)
            
        if res.status_code == 200:
            task_id = res.json()["task_id"]
            st.success(f"✅ 접수 완료! (작업번호: {task_id}) 이제 창을 내려두셔도 분석은 계속됩니다.")
            
            # UI 요소 예약 (진행률 바, 텍스트)
            progress_bar = st.progress(0)
            status_text = st.empty()
            log_box = st.empty()
            
            # 2. 진동벨(Polling) 루프: 10초마다 서버에 상태 묻기
            while True:
                status_res = requests.get(f"{API_URL.rstrip('/')}/status/{task_id}")
                if status_res.status_code == 200:
                    data = status_res.json()
                    status = data["status"]
                    progress = data["progress"]
                    logs = data["logs"]
                    
                    # UI 업데이트
                    progress_bar.progress(progress / 100.0)
                    status_text.markdown(f"**현재 진행률: {progress}%**")
                    log_box.code("\n".join(logs[-5:])) # 최근 로그 5줄만 표시
                    
                    if status == "completed":
                        st.balloons()
                        st.success("🎉 모든 분석이 완벽하게 끝났습니다!")
                        
                        # 3. 다운로드 버튼 생성 (API에서 파일 가져오기)
                        dl_res = requests.get(f"{API_URL.rstrip('/')}/download/{task_id}")
                        st.download_button(
                            label="📥 최종 FTO 엑셀 리포트 다운로드",
                            data=dl_res.content,
                            file_name="FTO_Integrated_Report.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            type="primary"
                        )
                        break
                    elif status == "error":
                        st.error("🚨 서버에서 치명적인 에러가 발생했습니다. 로그를 확인하세요.")
                        break
                
                time.sleep(10) # 10초 대기 후 다시 확인 (네트워크 부하 방지)
        else:
            st.error("서버 연결에 실패했습니다.")
