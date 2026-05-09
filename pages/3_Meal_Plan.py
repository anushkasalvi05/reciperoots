import streamlit as st
import json
import os
from datetime import date, timedelta
from utils.theme import apply_theme, page_header

MEAL_PLAN_FILE = "data/meal_plan.json"
RECIPES_FILE = "data/recipes.json"

def load_json(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

def save_meal_plan(plan):
    os.makedirs("data", exist_ok=True)
    with open(MEAL_PLAN_FILE, "w") as f:
        json.dump(plan, f, indent=2)

def get_week_dates():
    today = date.today()
    # Find the most recent Friday
    days_since_friday = (today.weekday() - 4) % 7
    friday = today - timedelta(days=days_since_friday)
    return [friday + timedelta(days=i) for i in range(7)]

st.set_page_config(page_title="Meal Plan", page_icon="📅", layout="wide")
apply_theme()
page_header("📅", "Meal Plan", "Plan your meals for the week — Friday to Thursday")

recipes = load_json(RECIPES_FILE)
meal_plan = load_json(MEAL_PLAN_FILE)
recipe_names = ["-- None --"] + [r["name"] for r in recipes]

week_dates = get_week_dates()
meal_types = ["Breakfast", "Lunch", "Dinner", "Snack"]

# Convert meal plan list to dict for easy lookup
plan_dict = {}
for entry in meal_plan:
    plan_dict[(entry["date"], entry["meal_type"])] = entry

st.markdown("### 🗓️ This week's plan")
st.caption(f"{week_dates[0].strftime('%d %b')} — {week_dates[-1].strftime('%d %b %Y')}")
st.markdown("---")

updated_plan = []

for day in week_dates:
    day_str = day.strftime("%A, %d %b")
    date_key = day.isoformat()

    st.markdown(f"### {day_str}")
    cols = st.columns(4)

    for i, meal in enumerate(meal_types):
        with cols[i]:
            st.markdown(f"**{meal}**")
            existing = plan_dict.get((date_key, meal), {})
            current_recipe = existing.get("recipe", "-- None --")

            if current_recipe not in recipe_names:
                current_recipe = "-- None --"

            selected = st.selectbox(
                meal,
                recipe_names,
                index=recipe_names.index(current_recipe),
                key=f"{date_key}_{meal}",
                label_visibility="collapsed"
            )

            notes = st.text_input(
                "Notes",
                value=existing.get("notes", ""),
                placeholder="e.g. make extra",
                key=f"notes_{date_key}_{meal}",
                label_visibility="collapsed"
            )

            if selected != "-- None --":
                # Find cuisine for selected recipe
                recipe_data = next((r for r in recipes if r["name"] == selected), {})
                cuisine = recipe_data.get("cuisine", "")
                st.caption(f"🍽️ {cuisine}")

            updated_plan.append({
                "date": date_key,
                "meal_type": meal,
                "recipe": selected,
                "notes": notes
            })

    st.markdown("---")

if st.button("💾 Save Meal Plan", type="primary"):
    save_meal_plan(updated_plan)
    st.success("✅ Meal plan saved!")
    st.rerun()