import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 제목
st.set_page_config(page_title="🇪🇸 바르셀로나 관광 지도", page_icon="🌍")
st.title("🇪🇸 바르셀로나 관광 명소 추천")
st.write("한국인이 좋아하는 바르셀로나의 주요 관광지와 맛집을 소개합니다!")

# 바르셀로나 중심 좌표
barcelona_coords = [41.3874, 2.1686]
m = folium.Map(location=barcelona_coords, zoom_start=13)

# 관광 명소 마커
tourist_spots = [
    {
        "name": "사그라다 파밀리아 성당",
        "location": [41.4036, 2.1744],
        "description": "가우디의 대표작, 바르셀로나의 상징"
    },
    {
        "name": "구엘 공원",
        "location": [41.4145, 2.1527],
        "description": "알록달록한 모자이크가 아름다운 공원"
    },
    {
        "name": "카사 바트요",
        "location": [41.3916, 2.1649],
        "description": "용을 닮은 지붕과 창문, 가우디 건축물 중 인기 많은 명소"
    }
]

for spot in tourist_spots:
    folium.Marker(
        location=spot["location"],
        popup=f"<b>{spot['name']}</b><br>{spot['description']}",
        tooltip=spot["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 맛집 마커 (예: 한국인이 즐겨찾는 현지 레스토랑)
folium.Marker(
    location=[41.3809, 2.1774],
    popup="<b>Ciudad Condal</b><br>타파스 맛집, 현지인과 관광객 모두가 추천!",
    tooltip="맛집: Ciudad Condal",
    icon=folium.Icon(color="red", icon="star")
).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)
