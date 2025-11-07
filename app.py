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
with tab3:
    st.header("🗺️ Titanic Route Map (Folium)")

    st.write("""
        This interactive map shows the approximate route of the RMS Titanic:
        **Southampton → Cherbourg → Queenstown (Cobh) → Intended destination: New York City**.
    """)

    # Coordinates (latitude, longitude)
    ports = {
        "Southampton, UK": [50.9097, -1.4044],
        "Cherbourg, France": [49.6341, -1.6222],
        "Queenstown (Cobh), Ireland": [51.8496, -8.2945],
        "New York City, USA": [40.7128, -74.0060]
    }

    # Initialize Folium map centered roughly mid-Atlantic
    m = folium.Map(location=[45, -30], zoom_start=3, tiles="CartoDB positron")

    # Add markers for each port
    for name, coords in ports.items():
        folium.Marker(
            location=coords,
            popup=f"<b>{name}</b>",
            icon=folium.Icon(color="blue", icon="ship", prefix="fa")
        ).add_to(m)

    # Add route line
    folium.PolyLine(
        locations=list(ports.values()),
        color="red",
        weight=3,
        opacity=0.8,
        tooltip="Titanic Route"
    ).add_to(m)

    # Display Folium map inside Streamlit
    st_folium(m, width=700, height=500)

# --- Footer ---
st.divider()
st.caption("© 2025 Example Streamlit App | Built with ❤️ and Streamlit | Data: Historical Titanic Route")
