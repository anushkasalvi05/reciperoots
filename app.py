import streamlit as st

st.set_page_config(
    page_title="RecipeRoots",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap');

.hero { padding: 3rem 0 2rem 0; }
.hero-label { font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 500; letter-spacing: 0.15em; text-transform: uppercase; color: #7C9E6E; margin-bottom: 12px; }
.hero-title { font-family: 'Playfair Display', serif; font-size: 52px; font-weight: 400; color: #1A1A1A; line-height: 1.15; margin-bottom: 16px; }
.hero-title em { font-style: italic; color: #7C9E6E; }
.hero-tagline { font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 300; color: #666; line-height: 1.7; max-width: 480px; margin-bottom: 2.5rem; }
.divider { height: 0.5px; background: #E8E8E8; margin: 2rem 0; }
.section-label { font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 500; letter-spacing: 0.15em; text-transform: uppercase; color: #AAA; margin-bottom: 1.5rem; }
.footer-note { font-family: 'Inter', sans-serif; font-size: 12px; color: #AAA; text-align: center; padding: 2rem 0 0.5rem; letter-spacing: 0.05em; }

div[data-testid="stButton"] button {
    width: 100%;
    height: auto;
    padding: 1.5rem 1.25rem !important;
    text-align: left !important;
    background: #fff !important;
    border: 0.5px solid #E8E8E8 !important;
    border-radius: 12px !important;
    transition: all 0.15s ease !important;
}
div[data-testid="stButton"] button:hover {
    border-color: #7C9E6E !important;
    background: #F8FCF6 !important;
    transform: translateY(-2px);
}
</style>

<div class="hero">
  <div class="hero-label">Your personal kitchen companion</div>
  <div class="hero-title">Where family recipes<br>meet <em>weekly planning.</em></div>
  <div class="hero-tagline">Save recipes from Instagram, preserve your mother's classics, track your pantry, and never wonder "what's for dinner?" again.</div>
</div>

<div class="divider"></div>
<div class="section-label">Navigate to</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🥫\n\n**Pantry**\n\nTrack everything at home"):
        st.switch_page("pages/1_Pantry.py")

with col2:
    if st.button("📖\n\n**Recipes**\n\nSave from Instagram, YouTube, or family"):
        st.switch_page("pages/2_Recipes.py")

with col3:
    if st.button("📅\n\n**Meal Plan**\n\nPlan every meal Friday to Thursday"):
        st.switch_page("pages/3_Meal_Plan.py")

with col4:
    if st.button("🛒\n\n**Grocery List**\n\nAuto-generated from your plan and pantry"):
        st.switch_page("pages/4_Grocery_List.py")

with col5:
    if st.button("👨‍🍳\n\n**Meal Prep**\n\nKnow exactly what to prep in advance"):
        st.switch_page("pages/5_Meal_Prep.py")

st.markdown("""
<div class="footer-note">Made with love by your dearest procrastinator</div>
""", unsafe_allow_html=True)