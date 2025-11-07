import streamlit as st
import folium
from streamlit_folium import st_folium 

# --- Page setup ---
st.set_page_config(page_title="Titanic Route Map", page_icon="🛳️", layout="centered")
st.title("🗺️ Titanic Route Map (Historical Waypoints with Sinking Point)")

tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Analytics", "🚢 Titanic Route"])

# --- Tab 1: Home ---
with tab1:
    st.header("Welcome")
    st.write("Placeholder content for Home tab.")

# --- Tab 2: Analytics ---
with tab2:
    st.header("Analytics")
    st.write("Placeholder content for Analytics tab.")
    st.metric(label="Sample Metric", value=42, delta=+3)
    st.progress(70)

# --- Tab 3: Titanic Route ---
with tab3:
    st.header("Titanic Route Map")
    st.write("""
        This map shows the Titanic's route using historical waypoints.
        Red line: reached route (including sinking point)  
        Green dashed line: planned/unreached route  
        Blue markers: reached points  
        Black marker: sinking point  
        Green markers: planned/unreached points  
        Background map: CartoDB Voyager (soft and pleasant)
    """)

    # Coordinates from ET article
    coords = [
        ("Daunt’s Rock LV",      [51 + 43/60,  -8 - 16/60]),
        ("Old Head of Kinsale (turn)", [51 + 33/60, -8 - 32/60]),
        ("Fastnet Light",        [51 + 23/60, -9 - 36/60]),
        ("Noon Apr 12",          [50 + 6/60, -20 - 43/60]),
        ("Noon Apr 13",          [47 + 22/60, -33 - 10/60]),
        ("Noon Apr 14",          [43 + 2/60, -44 - 31/60]),
        ("Corner (42°N,47°W)",   [42.0, -47.0]),
        ("Sinking Point",         [41 + 43/60, -49 - 56/60]),
        ("South of Nantucket Shoals", [40 + 35/60, -69 - 36.5/60]),
        ("Intended Destination: New York", [40.7128, -74.0060])
    ]

    # Create Folium map with CartoDB Voyager background
    m = folium.Map(location=[45, -40], zoom_start=3, tiles="CartoDB.DarkMatter")

    # Add markers
    for i, (name, coord) in enumerate(coords):
        if i <= 6:  # First 7 reached points
            folium.Marker(
                location=coord,
                popup=f"<b>{name}</b>",
                icon=folium.Icon(color="blue", icon="ship", prefix="fa")
            ).add_to(m)
        elif i == 7:  # Sinking point
            folium.Marker(
                location=coord,
                popup=f"<b>{name}</b>",
                icon=folium.Icon(color="black", icon="exclamation-triangle", prefix="fa")
            ).add_to(m)
        else:  # Planned/unreached
            folium.Marker(
                location=coord,
                popup=f"<b>{name}</b>",
                icon=folium.Icon(color="green", icon="flag", prefix="fa")
            ).add_to(m)

    # Red line: first 7 coords + sinking point
    folium.PolyLine(
        locations=[coord for _, coord in coords[:8]],
        color="red",
        weight=3,
        opacity=0.8,
        tooltip="Titanic Route (Reached)"
    ).add_to(m)

    # Green dashed line: sinking point → last 2 planned points
    folium.PolyLine(
        locations=[coord for _, coord in coords[7:]],
        color="green",
        weight=3,
        opacity=0.8,
        tooltip="Titanic Planned Route (Unreached)",
        dash_array="5,10"
    ).add_to(m)

    # Display map
    st_folium(m, width=700, height=500)

# --- Footer ---
st.divider()
st.caption("© 2025 Titanic Route Map | Data from Encyclopedia Titanica")
