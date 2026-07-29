import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정을 넓게 사용
st.set_page_config(layout="wide")

# 작성하신 HTML 코드 전체를 텍스트로 넣습니다.
html_code = """
(여기에 이전 답변에서 작성해 드린 <html> 부터 </html> 까지의 전체 코드를 붙여넣기 하세요)
"""

# Streamlit 컴포넌트를 통해 HTML 렌더링 (높이는 화면에 맞게 조절)
components.html(html_code, height=800, scrolling=True)
