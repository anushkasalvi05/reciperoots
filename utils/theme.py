import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap');

    /* Global typography */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
    }
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400 !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #FAFAF8 !important;
        border-right: 0.5px solid #E8E8E8 !important;
    }
    [data-testid="stSidebar"] * {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
    }

    /* Page title */
    .page-title {
        font-family: 'Playfair Display', serif !important;
        font-size: 36px !important;
        font-weight: 400 !important;
        color: #1A1A1A !important;
        margin-bottom: 4px !important;
    }
    .page-caption {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #888;
        font-weight: 300;
        margin-bottom: 2rem;
        letter-spacing: 0.02em;
    }
    .section-label {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        font-weight: 500;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #AAA;
        margin: 1.5rem 0 0.75rem;
    }
    .divider {
        height: 0.5px;
        background: #E8E8E8;
        margin: 1.5rem 0;
    }

    /* Cards */
    .rr-card {
        background: #fff;
        border: 0.5px solid #E8E8E8;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 10px;
        transition: border-color 0.15s;
    }
    .rr-card:hover { border-color: #7C9E6E; }

    /* Status badges */
    .badge-green { background: #EAF3DE; color: #3B6D11; font-size: 11px; padding: 3px 10px; border-radius: 20px; font-weight: 500; font-family: 'Inter', sans-serif; }
    .badge-amber { background: #FAEEDA; color: #633806; font-size: 11px; padding: 3px 10px; border-radius: 20px; font-weight: 500; font-family: 'Inter', sans-serif; }
    .badge-red   { background: #FCEBEB; color: #791F1F; font-size: 11px; padding: 3px 10px; border-radius: 20px; font-weight: 500; font-family: 'Inter', sans-serif; }
    .badge-blue  { background: #E6F1FB; color: #0C447C; font-size: 11px; padding: 3px 10px; border-radius: 20px; font-weight: 500; font-family: 'Inter', sans-serif; }

    /* Buttons */
    div[data-testid="stButton"] button {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        border-radius: 8px !important;
        border: 0.5px solid #E0E0E0 !important;
        transition: all 0.15s !important;
    }
    div[data-testid="stButton"] button:hover {
        border-color: #7C9E6E !important;
        background: #F8FCF6 !important;
    }

    /* Inputs */
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stSelectbox"] {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        border-radius: 8px !important;
    }

    /* Expander */
    [data-testid="stExpander"] {
        border: 0.5px solid #E8E8E8 !important;
        border-radius: 12px !important;
        background: #fff !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background: #FAFAF8;
        border: 0.5px solid #E8E8E8;
        border-radius: 10px;
        padding: 1rem !important;
    }
    
    /* Force expander background */
    [data-testid="stExpander"] details {
        background: #ffffff !important;
        border: 0.5px solid #E8E8E8 !important;
        border-radius: 12px !important;
    }
    [data-testid="stExpander"] details summary {
        background: #ffffff !important;
        border-radius: 12px !important;
    }

    /* Hide Streamlit default footer */
    footer { visibility: hidden; }

    /* Info/success/warning boxes */
    [data-testid="stAlert"] {
        border-radius: 10px !important;
        border: 0.5px solid #E8E8E8 !important;
        background: #FAFAF8 !important;
        color: #555 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
    }

    /* Expander header */
    [data-testid="stExpander"] summary {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #1A1A1A !important;
        letter-spacing: 0.02em !important;
    }

    /* Subheaders */
    [data-testid="stMarkdownContainer"] h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400 !important;
        font-size: 20px !important;
        color: #1A1A1A !important;
        margin-top: 1.5rem !important;
    }

    /* Radio buttons */
    [data-testid="stRadio"] label {
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
    }

    /* Select boxes */
    [data-testid="stSelectbox"] > div > div {
        border-radius: 8px !important;
        border: 0.5px solid #E0E0E0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
    }

    /* Number input */
    [data-testid="stNumberInput"] input {
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
    }

    /* Labels */
    [data-testid="stWidgetLabel"] p {
        font-family: 'Inter', sans-serif !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        color: #555 !important;
        letter-spacing: 0.03em !important;
    }
    </style>
    """, unsafe_allow_html=True)


def page_header(icon, title, caption):
    st.markdown(f"""
    <div style="padding: 1.5rem 0 0.5rem;">
        <div style="font-size:11px; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; color:#7C9E6E; margin-bottom:8px; font-family:'Inter',sans-serif;">RecipeRoots</div>
        <div style="font-family:'Playfair Display',serif; font-size:36px; font-weight:400; color:#1A1A1A; margin-bottom:6px;">{icon} {title}</div>
        <div style="font-family:'Inter',sans-serif; font-size:13px; color:#888; font-weight:300;">{caption}</div>
    </div>
    <div style="height:0.5px; background:#E8E8E8; margin:1rem 0 1.5rem;"></div>
    """, unsafe_allow_html=True)