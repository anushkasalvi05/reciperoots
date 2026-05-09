import streamlit as st

st.set_page_config(
    page_title="RecipeRoots",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🌿 RecipeRoots")
st.markdown("*Saving the recipes that matter, one meal at a time*")
st.markdown("---")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("### 🥫 Pantry")
    st.caption("Track what you have at home")

with col2:
    st.markdown("### 📖 Recipes")
    st.caption("Save from Instagram, YouTube or family")

with col3:
    st.markdown("### 📅 Meal Plan")
    st.caption("Plan your week Friday to Thursday")

with col4:
    st.markdown("### 🛒 Grocery List")
    st.caption("Auto-generated shopping list")

with col5:
    st.markdown("### 👨‍🍳 Meal Prep")
    st.caption("What to prep in advance")

st.markdown("---")
st.info("👈 Use the sidebar to navigate between sections.")