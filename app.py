import streamlit as st
import folium
from streamlit_folium import st_folium

# --- Page Setup ---
st.set_page_config(page_title="Three Tabs Demo", page_icon="🛳️", layout="centered")

# --- Title ---
st.title("🧭 Streamlit Three Tabs Example")
st.write("This is a simple demo app with three tabs and an interactive Folium map of the Titanic route.")

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Analytics", "🗺️ Titanic Route"])

# --- Tab 1: Home ---
with tab1:
    st.header("Welcome to the Home Tab")
    st.write("""
        This is placeholder content for the Home tab.
        You can add markdown, widgets, charts, or anything else here.
    """)
    st.markdown("> 💡 Tip: Streamlit updates instantly as you edit and save this file!")

# --- Tab 2: Analytics ---
with tab2:
    st.header("Analytics Overview")
    st.write("""
        This tab could later display charts, metrics, or data visualizations.
        For now, it just shows some filler text.
    """)
    st.metric(label="Sample Metric", value="42", delta="+3")
    st.progress(70)

# --- Tab 3: Titanic Route (Folium Map) ---
import streamlit as st
import folium
from streamlit_folium import st_folium
import math

def make_map():
    # Waypoints approximate the track
    waypoints = [
        ("Southampton, UK",    [50.9097, -1.4044]),
        ("Cherbourg, France",  [49.6341, -1.6222]),
        ("Queenstown (Cobh)",  [51.8496, -8.2945]),
        # “Corner” point
        ("The Corner (42°N,47°W)", [42.0, -47.0]),
        # Point near Nantucket Shoals
        ("South of Nantucket Shoals", [40.5833, -69.6083]),
        # Iceberg collision approximate
        ("Collision Point (~41°46′N,49°56′W)", [41.7667, -49.9333]),
        # Wreck site
        ("Wreck Site (~41°43′N,49°56′W)",   [41.7167, -49.9333]),
        # Optional: Intended destination (NY)
        ("Intended Destination: New York City", [40.7128, -74.0060]),
    ]

    m = folium.Map(location=[45, -40], zoom_start=3, tiles="CartoDB positron")

    # Add markers
    for name, coords in waypoints:
        folium.Marker(
            location=coords,
            popup=f"<b>{name}</b>",
            icon=folium.Icon(color="blue", icon="ship", prefix="fa")
        ).add_to(m)

    # Polyline through waypoints (makes a more realistic curved route)
    locations = [coords for name, coords in waypoints]
    folium.PolyLine(locations=locations,
                    color="red",
                    weight=3,
                    opacity=0.8,
                    tooltip="Approximate Titanic Track").add_to(m)

    return m

with tab3:
    st.header("🗺️ Titanic Route Map (Approximate Actual Track)")
    st.write("""
        This map uses known navigational waypoints of the Titanic’s maiden voyage, including
        stops and the point of collision. It is an approximation — the exact continuous track is not publicly available.
    """)
    m = make_map()
    st_folium(m, width=700, height=500)

