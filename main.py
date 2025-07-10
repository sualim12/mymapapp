import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="🇪🇸 바르셀로나 관광 지도", page_icon="🌍")
st.title("🇪🇸 바르셀로나 관광 명소 & 맛집 가이드")
st.write("한국인 여행객에게 인기 있는 바르셀로나 명소와 맛집을 소개합니다! ✨")

# 지도 생성
barcelona_coords = [41.3874, 2.1686]
m = folium.Map(location=barcelona_coords, zoom_start=13)

# 관광지 정보 리스트
tourist_spots = [
    {
        "name": "⛪ 사그라다 파밀리아 성당",
        "location": [41.4036, 2.1744],
        "description": "가우디의 걸작이자 바르셀로나의 상징인 성당입니다. 독특한 첨탑과 내부 빛의 연출은 꼭 직접 경험해보세요!",
    },
    {
        "name": "🌳 구엘 공원",
        "location": [41.4145, 2.1527],
        "description": "형형색색 모자이크 타일과 자연이 어우러진 예술 공원입니다. 인생샷 명소로 유명합니다!",
    },
    {
        "name": "🏠 카사 바트요",
        "location": [41.3916, 2.1649],
        "description": "용의 등뼈를 닮은 지붕과 유기적인 곡선미가 특징인 건축물로, 가우디의 상상력이 돋보이는 명소입니다.",
    }
]

# 마커 표시 및 설명 출력
st.subheader("📍 추천 관광지")
for spot in tourist_spots:
    st.markdown(f"### {spot['name']}")
    st.write(spot["description"])
    folium.Marker(
        location=spot["location"],
        popup=f"<b>{spot['name']}</b><br>{spot['description']}",
        tooltip=spot["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 맛집
st.subheader("🍽 추천 맛집")
st.markdown("### 🍷 씨우닷 콘달 (Ciudad Condal)")
st.write("바르셀로나 타파스 맛집 중 손꼽히는 곳으로, 고등어 타파스와 감바스 알 아히요가 인기 메뉴입니다. 평일 저녁엔 줄이 길 수 있으니 예약 추천! 😉")

folium.Marker(
    location=[41.3809, 2.1774],
    popup="<b>🍷 Ciudad Condal</b><br>현지인도 극찬하는 타파스 맛집!",
    tooltip="맛집: Ciudad Condal",
    icon=folium.Icon(color="red", icon="star")
).add_to(m)

# 지도 출력
st.subheader("🗺️ 바르셀로나 지도")
st_folium(m, width=700, height=500)
