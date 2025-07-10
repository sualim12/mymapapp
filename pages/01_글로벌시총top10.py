# streamlit_app.py

import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go

# 페이지 기본 설정
st.set_page_config(page_title="글로벌 시가총액 TOP 10 주가 그래프", page_icon="📈")
st.title("📈 글로벌 시가총액 TOP 10 기업 - 최근 3년 주가 변동")

# 시가총액 기준 TOP 10 기업 (2025년 기준 추정)
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

# 기간 설정: 최근 3년
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)

# Plotly 그래프 초기화
fig = go.Figure()

# 기업별 주가 데이터를 그래프에 추가
for name, ticker in top10_companies.items():
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            st.warning(f"{name} ({ticker})의 데이터를 가져올 수 없습니다.")
            continue
        # 월 단위 평균 종가로 리샘플링
        data_monthly = data['Close'].resample('M').mean()
        fig.add_trace(go.Scatter(x=data_monthly.index, y=data_monthly.values,
                                 mode='lines', name=name))
    except Exception as e:
        st.error(f"{name}의 데이터를 불러오는 중 오류 발생: {e}")

# 그래프 스타일 설정
fig.update_layout(
    title="최근 3년간 글로벌 시가총액 TOP 10 기업의 월별 평균 주가",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    legend_title="기업명",
    hovermode="x unified"
)

# Streamlit에 그래프 출력
st.plotly_chart(fig, use_container_width=True)
