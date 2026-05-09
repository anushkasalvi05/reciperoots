import streamlit as st
import json
import os
from utils.theme import apply_theme, page_header

MEAL_PLAN_FILE = "data/meal_plan.json"
RECIPES_FILE = "data/recipes.json"

def load_json(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

st.set_page_config(page_title="Meal Prep", page_icon="👨‍🍳", layout="wide")
apply_theme()
page_header("👨‍🍳", "Meal Prep", "What to prepare in advance for the week")

meal_plan = load_json(MEAL_PLAN_FILE)
recipes = load_json(RECIPES_FILE)
recipe_lookup = {r["name"]: r for r in recipes}

# Collect all recipes planned for the week
planned_recipes = {}
for entry in meal_plan:
    recipe_name = entry.get("recipe", "-- None --")
    if recipe_name == "-- None --":
        continue
    day = entry.get("date", "")
    meal_type = entry.get("meal_type", "")
    if recipe_name not in planned_recipes:
        planned_recipes[recipe_name] = []
    planned_recipes[recipe_name].append(f"{meal_type} on {day}")

if not planned_recipes:
    st.info("No meals planned yet. Go to the Meal Plan page and plan your week first!")
else:
    st.markdown("### 📋 This week's prep checklist")
    st.caption("Based on your meal plan — check off as you prep!")
    st.markdown("---")

    # Keywords that suggest prep is needed
    prep_keywords = [
        "soak", "marinate", "chop", "dice", "slice", "boil", "blanch",
        "grind", "blend", "knead", "rest", "chill", "freeze", "overnight",
        "ferment", "sprout", "pressure cook", "roast", "toast", "crush"
    ]

    has_prep = False

    for recipe_name, meal_slots in planned_recipes.items():
        recipe = recipe_lookup.get(recipe_name, {})
        steps = recipe.get("steps", "")
        ingredients = recipe.get("ingredients", "")
        notes = recipe.get("notes", "")
        prep_time = recipe.get("prep_time", "")
        cuisine = recipe.get("cuisine", "")

        # Find steps that involve prep
        prep_steps = []
        for line in steps.split("\n"):
            if any(kw in line.lower() for kw in prep_keywords):
                prep_steps.append(line.strip())

        # Find ingredients that need prep
        prep_ingredients = []
        for line in ingredients.split("\n"):
            if any(kw in line.lower() for kw in ["soaked", "overnight", "marinated", "chopped", "diced"]):
                prep_ingredients.append(line.strip())

        with st.container():
            st.markdown(f"### 🍽️ {recipe_name}")
            col1, col2 = st.columns(2)
            with col1:
                st.caption(f"🍴 {cuisine} · ⏱️ {prep_time}")
                st.caption(f"📅 Planned for: {', '.join(meal_slots)}")
            with col2:
                if notes:
                    st.info(f"📝 {notes}")

            if prep_steps or prep_ingredients:
                has_prep = True
                st.markdown("**Prep needed:**")
                for step in prep_steps:
                    checked = st.checkbox(step, key=f"prep_step_{recipe_name}_{step[:20]}")
                for ing in prep_ingredients:
                    checked = st.checkbox(f"Prep ingredient: {ing}", key=f"prep_ing_{recipe_name}_{ing[:20]}")
            else:
                st.success("✅ No advance prep needed — cook fresh!")

            st.markdown("**Full ingredients:**")
            st.code(ingredients, language=None)

            st.markdown("---")

    if not has_prep:
        st.balloons()
        st.success("🎉 Great news — none of your meals this week need advance prep!")