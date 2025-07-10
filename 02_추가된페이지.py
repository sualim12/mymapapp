# streamlit_app.py

import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="글로벌 시가총액 TOP 10 주가 및 AI 기업 소개", page_icon="📈")
st.title("📈 글로벌 시가총액 TOP 10 기업 - 최근 3년 주가 및 차세대 AI 기업 소개")

# 주요 기업 설정
top10_companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Berkshire Hathaway': 'BRK-B',
    'Meta (Facebook)': 'META',
    'TSMC': 'TSM',
    'Tesla': 'TSLA'
}

# 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=3 * 365)

# 주가 추세 그래프 초기화
st.subheader("📊 최근 3년간 주가 추세")
fig = go.Figure()

market_caps = {}

for name, ticker in top10_companies.items():
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            st.warning(f"{name} ({ticker})의 데이터를 가져올 수 없습니다.")
            continue
        # 월별 평균 종가
        data_monthly = data['Close'].resample('M').mean()
        fig.add_trace(go.Scatter(x=data_monthly.index, y=data_monthly.values,
                                 mode='lines', name=name))
        
        # 시가총액 정보 수집
        info = yf.Ticker(ticker).info
        market_caps[name] = info.get('marketCap', None)
        
    except Exception as e:
        st.error(f"{name}의 데이터 처리 중 오류 발생: {e}")

fig.update_layout(
    title="최근 3년간 월별 평균 주가 추이",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    legend_title="기업명",
    hovermode="x unified"
)
st.plotly_chart(fig, use_container_width=True)

# 시가총액 막대 그래프
st.subheader("🏢 기업별 시가총액 비교 (2025년 기준)")

cap_df = pd.DataFrame({
    '기업명': list(market_caps.keys()),
    '시가총액 (조 달러)': [cap / 1e12 if cap else None for cap in market_caps.values()]
}).dropna().sort_values(by='시가총액 (조 달러)', ascending=False)

fig_bar = px.bar(cap_df, x='기업명', y='시가총액 (조 달러)', text='시가총액 (조 달러)',
                 title="글로벌 시가총액 TOP 10 기업 비교",
                 labels={'시가총액 (조 달러)': '시가총액 (조 달러)'})
st.plotly_chart(fig_bar, use_container_width=True)

# 차세대 AI 기업 정보 추가
st.subheader("🤖 차세대 AI 주요 기업 소개")

ai_companies = {
    "Nvidia": "AI 반도체 및 GPU 시장의 선도 기업",
    "Palantir": "정부·기업 대상 데이터 분석 및 AI 플랫폼",
    "AMD": "Nvidia의 경쟁사, AI 연산 가속기 개발 중",
    "Snowflake": "AI 및 데이터 클라우드 기반 플랫폼 제공",
    "OpenAI (비상장)": "GPT 모델 개발사, Microsoft의 전략적 파트너",
    "Anthropic (비상장)": "Claude 모델 개발사, Google·Amazon 투자",
    "Hugging Face (비상장)": "오픈소스 AI 모델의 중심 플랫폼",
}

for name, desc in ai_companies.items():
    st.markdown(f"**🔹 {name}**: {desc}")
