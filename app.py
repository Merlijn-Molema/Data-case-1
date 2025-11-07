import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# --- Page setup ---
st.set_page_config(page_title="Titanic Route Map", page_icon="🛳️", layout="centered")
st.title("🗺️ Titanic Route Map (Passenger Pickup Route + Voyage)")

# Reorder tabs: Map first
tab_map, tab_home, tab_analytics = st.tabs(["De Titanic", "🏠 Home", "📊 Analytics"])

# --- Tab 1: Titanic Route Map ---
with tab_map:
    st.header("De Titanic")
    st.write("""
        De RMS Titanic vertrok op 10 april 1912 vanuit Southampton, Engeland, met als bestemming New York, Verenigde Staten.
        De geplande route leidde de Titanic langs de kust van Engeland, Frankrijk en Ierland, waarna het schip de Atlantische Oceaan overstak. 
        Onderweg maakte het een korte stop in Cherbourg, Frankrijk, en daarna in Queenstown (nu Cobh), Ierland, om extra passagiers en post op te nemen.
        De oversteek verliep aanvankelijk rustig, maar op 14 april 1912, rond 23:40 uur, raakte de Titanic een ijsberg in het noorden van de Atlantische Oceaan, ongeveer 600 kilometer ten zuiden van Newfoundland, Canada. 
        De botsing veroorzaakte grote schade aan de scheepsromp en leidde uiteindelijk tot het zinken van het schip in de vroege ochtend van 15 april 1912.
        ijdens de ramp probeerde de bemanning de passagiers zo goed mogelijk in reddingsboten te krijgen, maar door een tekort aan boten en chaos aan boord konden niet alle mensen worden gered. 
        **Van de ongeveer 2.224 mensen aan boord overleefden ongeveer 710 passagiers.**
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
        ("Punt van zinken",         [41 + 43/60, -49 - 56/60]),
        ("Zuid van Nantucket Shoals", [40 + 35/60, -69 - 36.5/60]),
        ("Bestemming: New York", [40.7128, -74.0060])
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
            popup=f"<b>{name} (Passagiers afhalen)</b>",
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
        tooltip="Passagiers boarding Route"
    ).add_to(m)

    # Red line: first 7 coords + sinking point
    folium.PolyLine(
        locations=[coord for _, coord in coords[:8]],
        color="red",
        weight=3,
        opacity=0.8,
        tooltip="afgelegde route"
    ).add_to(m)

    # Green dashed line: sinking point → last 2 planned points
    folium.PolyLine(
        locations=[coord for _, coord in coords[7:]],
        color="green",
        weight=3,
        opacity=0.8,
        tooltip="geplande route",
        dash_array="5,10"
    ).add_to(m)

    # Display map
    st_folium(m, width=700, height=500)

# --- Tab 2: Home ---
with tab_home:
    st.header("Welcome")
    st.write("Placeholder content for Home tab.")

# --- Tab 3: Analytics ---
with tab_analytics:
    st.header("Het maken van een voorspelling")
    st.write("""Het maken van een voorspelling begint met een nette dataset, hiermee is ook de eerste stap om alle missende waardes weg te werken, 
                de intieele data van Kaggle komt met 12 kolomen waarvan somig missende data bevatten:""")
    data = {
    "PassengerId": [0],
    "Survived": [0],
    "Pclass": [0],
    "Name": [0],
    "Sex": [0],
    "Age": [177],
    "SibSp": [0],
    "Parch": [0],
    "Fare": [0],
    "Cabin": [687],
    "Embarked": [2]
    }
    df = pd.DataFrame(data)
    # Transpose and reset index for better display
    df_transposed = df.T.reset_index()
    df_transposed.columns = ["Attribute", "Value"]
    st.table(df_transposed)
# --- Footer ---
st.divider()
st.caption("© 2025 Titanic Route Map | Data from Encyclopedia Titanica")
