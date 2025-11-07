import streamlit as st

# Page setup
st.set_page_config(page_title="Two Tabs Demo", page_icon="🧭", layout="centered")

# App title
st.title("🧭 Streamlit Two Tabs Example")
st.write("This is a simple demo app with two tabs and filler text. You can extend it as needed.")

# Tabs
tab1, tab2 = st.tabs(["🏠 Home", "📊 Analytics"])

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

# Footer
st.divider()
st.caption("© 2025 Example Streamlit App | Built with ❤️ and Streamlit")
