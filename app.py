import streamlit as st
import folium
from streamlit_folium import st_folium

# --- Page setup ---
st.set_page_config(page_title="Titanic Route Map", page_icon="🛳️", layout="centered")
st.title("🗺️ Titanic Route Map (Passenger Pickup Route + Voyage)")

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
        This map shows the Titanic's route using historical waypoints from Encyclopedia Titanica.
        - Purple line: passenger pickup route (Southampton → Cherbourg → Cobh → Daunt’s Rock LV), smoothed along Channel & Celtic Sea  
        - Red line: reached route (including sinking point)  
        - Green dashed line: planned/unreached route  
        - Blue markers: reached points  
        - Black marker: sinking point  
        - Green markers: planned/unreached points  
        - Purple markers: passenger pickup points  
        Background map: Esri NatGeo World Map
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

    # Passenger pickup points
    pickup_points = [
        ("Southampton, UK", [50.9097, -1.4044]),
        ("Cherbourg, France", [49.6341, -1.6222]),
        ("Queenstown (Cobh), Ireland", [51.8496, -8.2945])
    ]

    # Create Folium map
    m = folium.Map(location=[45, -40], zoom_start=3, tiles="Esri.NatGeoWorldMap")

    # Add reached points (blue)
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

    # Add pickup markers (purple) at Southampton, Cherbourg, Cobh only
    for name, coord in pickup_points:
        folium.Marker(
            location=coord,
            popup=f"<b>{name} (Passenger Pickup)</b>",
            icon=folium.Icon(color="purple", icon="user", prefix="fa")
        ).add_to(m)

    # Smooth purple line with adjusted first segment southeastward
    pickup_route = [
        pickup_points[0][1],        # Southampton
        [50.5, -0.76], [50.2, -0.7], [50, -0.9],  # southeastward curve before Cherbourg
        pickup_points[1][1],        # Cherbourg
        [49.9, -2.0], [49.8, -2.3], [49.7, -2.6], [49.6, -3.0],
        [49.5, -3.5], [49.4, -4.0], [49.4, -4.5], [49.5, -5.0],
        [49.7, -5.5], [50.0, -6.0], [50.3, -6.5], [50.6, -7.0],
        [51.0, -7.3], [51.4, -7.7],
        pickup_points[2][1],        # Cobh
        coords[0][1]                # Daunt's Rock LV
    ]

    folium.PolyLine(
        locations=pickup_route,
        color="purple",
        weight=3,
        opacity=0.8,
        tooltip="Passenger Pickup Route (Smooth maritime path)"
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
