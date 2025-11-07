import streamlit as st
import folium
from streamlit_folium import st_folium

# Page setup
st.set_page_config(page_title="Titanic Route Map", page_icon="🛳️", layout="centered")

st.title("🗺️ Titanic Route Map (Historical Waypoints with Sinking Point)")

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
        This map shows the Titanic's historical route, with reached points marked in blue,
        the sinking location in black, and planned/unreached points (New York) in green.
        Data from Encyclopedia Titanica: [Link](https://www.encyclopedia-titanica.org/keeping-track.html)
    """)

    # Reached waypoints (actual voyage before sinking)
    reached_points = [
        ("Daunt’s Rock LV",      [51 + 43/60,  -8 - 16/60]),  # 51°43' N, 08°16' W
        ("Old Head of Kinsale (turn)", [51 + 33/60, -8 - 32/60]),
        ("Fastnet Light",        [51 + 23/60, -9 - 36/60]),
        ("Noon Apr 12",          [50 + 6/60, -20 - 43/60]),
        ("Noon Apr 13",          [47 + 22/60, -33 - 10/60]),
        ("Noon Apr 14",          [43 + 2/60, -44 - 31/60]),
        ("Corner (42°N,47°W)",   [42.0, -47.0]),
        ("South of Nantucket Shoals", [40 + 35/60, -69 - 36.5/60]),
        ("Ambrose Channel LV",   [40 + 28/60, -73 - 50/60]),
    ]

    # Sinking point
    sinking_point = ("Sinking Point", [41 + 43/60, -49 - 56/60])  # 41°43′ N, 49°56′ W

    # Planned / unreached point
    planned_points = [
        ("Intended Destination: New York", [40.7128, -74.0060])
    ]

    # Create map
    m = folium.Map(location=[45, -40], zoom_start=3, tiles="CartoDB positron")

    # Add reached points
    for name, coords in reached_points:
        folium.Marker(
            location=coords,
            popup=f"<b>{name}</b>",
            icon=folium.Icon(color="blue", icon="ship", prefix="fa")
        ).add_to(m)

    # Add sinking point
    folium.Marker(
        location=sinking_point[1],
        popup=f"<b>{sinking_point[0]}</b>",
        icon=folium.Icon(color="black", icon="exclamation-triangle", prefix="fa")
    ).add_to(m)

    # Add planned / unreached points
    for name, coords in planned_points:
        folium.Marker(
            location=coords,
            popup=f"<b>{name}</b>",
            icon=folium.Icon(color="green", icon="flag", prefix="fa")
        ).add_to(m)

    # Draw route line: reached points in red
    folium.PolyLine(
        locations=[coords for _, coords in reached_points],
        color="red",
        weight=3,
        opacity=0.8,
        tooltip="Titanic Route (Reached)"
    ).add_to(m)

    # Optional: dashed line from sinking point to planned destination
    folium.PolyLine(
        locations=[sinking_point[1], planned_points[0][1]],
        color="green",
        weight=3,
        opacity=0.5,
        tooltip="Planned Route (Unreached)",
        dash_array="5,10"
    ).add_to(m)

    # Display map
    st_folium(m, width=700, height=500)

st.divider()
st.caption("© 2025 Titanic Route Map | Data from Encyclopedia Titanica")
