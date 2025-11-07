import streamlit as st
import plotly.graph_objects as go

# --- Page Setup ---
st.set_page_config(page_title="Three Tabs Demo", page_icon="🛳️", layout="centered")

# --- Title ---
st.title("🧭 Streamlit Three Tabs Example")
st.write("This is a simple demo app with three tabs and an interactive map of the Titanic route.")

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

# --- Tab 3: Titanic Route ---
with tab3:
    st.header("🗺️ Titanic Route Map")

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

    lats = [v[0] for v in ports.values()]
    lons = [v[1] for v in ports.values()]
    names = list(ports.keys())

    # Plotly map figure
    fig = go.Figure()

    # Route line
    fig.add_trace(go.Scattergeo(
        lon=lons,
        lat=lats,
        mode='lines+markers+text',
        text=names,
        textposition="top center",
        line=dict(width=2, color="blue"),
        marker=dict(size=8, color="red"),
    ))

    # Layout
    fig.update_layout(
        title="RMS Titanic Route (1912)",
        geo=dict(
            projection_type="natural earth",
            showcountries=True,
            showcoastlines=True,
            showland=True,
            landcolor="rgb(243, 243, 243)",
            countrycolor="rgb(204, 204, 204)",
        ),
        height=500
    )

    # Display interactive map
    st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.divider()
st.caption("© 2025 Example Streamlit App | Built with ❤️ and Streamlit | Data: Historical Titanic Route")
