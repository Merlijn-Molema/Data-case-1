import streamlit as st
import folium
from streamlit_folium import st_folium

# Page setup
st.set_page_config(page_title="Titanic Route Map", page_icon="🛳️", layout="centered")

st.title("🗺️ Titanic Route Map (Historical Waypoints)")

tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Analytics", "🚢 Titanic Route"])

with tab1:
    st.header("Welcome")
    st.write("Placeholder content for Home tab.")

with tab2:
    st.header("Analytics")
    st.write("Placeholder content for Analytics tab.")
    st.metric(label="Sample Metric", value=42, delta=+3)
    st.progress(70)

with tab3:
    st.header("Titanic Route Map")
    st.write("""
        This map shows the approximate historical route of the Titanic from departure 
        off Daunt’s Rock Light Vessel, via waypoints including the “Corner”, 
        south of the Nantucket Shoals light vessel, etc. Data from Encyclopedia Titanica. :contentReference[oaicite:4]{index=4}
    """)

    # Historical waypoints per ET article
    waypoints = [
        ("Daunt’s Rock LV",      [51 + 43/60,  -8 - 16/60]),        # 51° 43’ N, 08° 16’ W :contentReference[oaicite:5]{index=5}
        ("Old Head of Kinsale (turn)", [51 + 33/60, -8 - 32/60]),    # 51° 33’ N, 08° 32’ W :contentReference[oaicite:6]{index=6}
        ("Fastnet Light",        [51 + 23/60, -9 - 36/60]),         # 51° 23’ N, 09° 36’ W :contentReference[oaicite:7]{index=7}
        ("Noon Apr 12",          [50 + 06/60, -20 - 43/60]),        # 50° 06’ N, 20° 43’ W :contentReference[oaicite:8]{index=8}
        ("Noon Apr 13",          [47 + 22/60, -33 - 10/60]),        # 47° 22’ N, 33° 10’ W :contentReference[oaicite:9]{index=9}
        ("Noon Apr 14",          [43 + 02/60, -44 - 31/60]),        # 43° 02’ N, 44° 31’ W :contentReference[oaicite:10]{index=10}
        ("Corner (42°N,47°W)",   [42.0,             -47.0]),         # 42° N, 47° W :contentReference[oaicite:11]{index=11}
        ("South of Nantucket Shoals", [40 + 35/60, -69 - 36.5/60]), # 40° 35’ N, 69° 36.5’ W :contentReference[oaicite:12]{index=12}
        ("Ambrose Channel LV",   [40 + 28/60, -73 - 50/60]),        # 40° 28’ N, 73° 50’ W :contentReference[oaicite:13]{index=13}
    ]

    # Create map
    m = folium.Map(location=[45, -40], zoom_start=3, tiles="CartoDB positron")

    # Add markers
    for name, coords in waypoints:
        folium.Marker(
            location=coords,
            popup=f"<b>{name}</b>",
            icon=folium.Icon(color="blue", icon="ship", prefix="fa")
        ).add_to(m)

    # Add route line
    folium.PolyLine(
        locations=[coords for _, coords in waypoints],
        color="red",
        weight=3,
        opacity=0.8,
        tooltip="Titanic Approximate Route"
    ).add_to(m)

    # Display map
    st_folium(m, width=700, height=500)

st.divider()
st.caption("© 2025 Titanic Route Map | Data from Encyclopedia Titanica")
