import streamlit as st
import json
import os

SETTINGS_FILE = "data/settings.json"

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {
            "cuisines": ["Indian", "Italian", "Indo-Chinese", "Continental", "Mexican", "Middle Eastern"],
            "grocery_email_day": "Friday",
            "email": ""
        }
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    os.makedirs("data", exist_ok=True)
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")
st.title("⚙️ Settings")
st.caption("Customise RecipeRoots to your taste")
st.markdown("---")

settings = load_settings()

# --- Cuisine tags ---
st.markdown("### 🍽️ Cuisine tags")
st.caption("These appear as options when adding recipes and planning meals")

cuisines = settings.get("cuisines", [])

col1, col2 = st.columns([3, 1])
with col1:
    new_cuisine = st.text_input("Add a new cuisine", placeholder="e.g. Thai, Ethiopian, Gujarati...")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("➕ Add"):
        if new_cuisine.strip() and new_cuisine.strip() not in cuisines:
            cuisines.append(new_cuisine.strip())
            settings["cuisines"] = cuisines
            save_settings(settings)
            st.success(f"✅ {new_cuisine} added!")
            st.rerun()

st.markdown("**Current cuisine tags:**")
cols = st.columns(4)
for i, cuisine in enumerate(cuisines):
    with cols[i % 4]:
        col_tag, col_del = st.columns([3, 1])
        with col_tag:
            st.markdown(f"🏷️ {cuisine}")
        with col_del:
            if st.button("✕", key=f"del_cuisine_{i}"):
                cuisines.remove(cuisine)
                settings["cuisines"] = cuisines
                save_settings(settings)
                st.rerun()

st.markdown("---")

# --- Grocery email settings ---
st.markdown("### 📧 Weekly grocery email")
st.caption("Get your grocery list emailed to you every week")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
current_day = settings.get("grocery_email_day", "Friday")
current_email = settings.get("email", "")

col1, col2 = st.columns(2)
with col1:
    email = st.text_input("Email address", value=current_email, placeholder="your@email.com")
with col2:
    email_day = st.selectbox(
        "Send every",
        days,
        index=days.index(current_day)
    )

if st.button("💾 Save email settings"):
    settings["grocery_email_day"] = email_day
    settings["email"] = email
    save_settings(settings)
    st.success(f"✅ Grocery list will be emailed to {email} every {email_day}!")

st.markdown("---")

# --- Data management ---
st.markdown("### 🗄️ Data")
st.caption("Manage your app data")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🗑️ Clear meal plan"):
        if os.path.exists("data/meal_plan.json"):
            os.remove("data/meal_plan.json")
            st.success("Meal plan cleared!")
            st.rerun()
with col2:
    if st.button("🗑️ Clear grocery list"):
        if os.path.exists("data/grocery.json"):
            os.remove("data/grocery.json")
            st.success("Grocery list cleared!")
            st.rerun()
with col3:
    if st.button("🗑️ Clear pantry"):
        if os.path.exists("data/pantry.json"):
            os.remove("data/pantry.json")
            st.success("Pantry cleared!")
            st.rerun()