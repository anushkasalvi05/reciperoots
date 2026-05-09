import streamlit as st
import json
import os
from utils.theme import apply_theme, page_header

RECIPES_FILE = "data/recipes.json"

def load_recipes():
    if not os.path.exists(RECIPES_FILE):
        return []
    with open(RECIPES_FILE, "r") as f:
        return json.load(f)

def save_recipes(recipes):
    os.makedirs("data", exist_ok=True)
    with open(RECIPES_FILE, "w") as f:
        json.dump(recipes, f, indent=2)

st.set_page_config(page_title="Recipes", page_icon="📖", layout="wide")
apply_theme()
page_header("📖", "Recipes", "Save recipes from Instagram, YouTube, or your family kitchen")

recipes = load_recipes()

# --- Add new recipe ---
with st.expander("➕ Add new recipe", expanded=False):
    source_type = st.radio(
        "Where is this recipe from?",
        ["📸 Instagram", "▶️ YouTube", "👩‍🍳 Family / My Own"],
        horizontal=True
    )

    if source_type in ["📸 Instagram", "▶️ YouTube"]:
        url = st.text_input("Paste the link here")
        if url and st.button("🔍 Fetch Recipe with AI"):
            with st.spinner("Fetching recipe..."):
                # Placeholder for Claude API call
                st.info("🚧 AI recipe fetching coming soon! For now, fill in the details manually below.")

    st.markdown("#### Recipe details")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Recipe name", placeholder="e.g. Masala Oats")
        cuisine = st.selectbox("Cuisine", [
            "Indian", "Italian", "Indo-Chinese", "Continental",
            "Mexican", "Middle Eastern", "Other"
        ])
        meal_type = st.multiselect("Meal type", [
            "Breakfast", "Lunch", "Dinner", "Snack"
        ])
    with col2:
        prep_time = st.text_input("Prep time", placeholder="e.g. 15 mins")
        source_label = st.text_input(
            "Source name (optional)",
            placeholder="e.g. Mom's recipe / @foodblogger"
        )
        source_url = st.text_input(
            "Source URL (optional)",
            placeholder="e.g. https://instagram.com/..."
        ) if source_type in ["📸 Instagram", "▶️ YouTube"] else ""

    ingredients = st.text_area(
        "Ingredients (one per line)",
        placeholder="500g oats\n2 cups milk\n1 tsp sugar"
    )
    steps = st.text_area(
        "Steps",
        placeholder="1. Boil milk\n2. Add oats\n3. Stir for 5 mins"
    )
    notes = st.text_area(
        "Notes (optional)",
        placeholder="Any tips, variations, or memories about this recipe..."
    )

    if st.button("💾 Save Recipe"):
        if name.strip() == "":
            st.warning("Please enter a recipe name.")
        else:
            recipes.append({
                "name": name.strip(),
                "cuisine": cuisine,
                "meal_type": meal_type,
                "prep_time": prep_time,
                "source_type": source_type,
                "source_label": source_label,
                "source_url": source_url,
                "ingredients": ingredients.strip(),
                "steps": steps.strip(),
                "notes": notes.strip()
            })
            save_recipes(recipes)
            st.success(f"✅ {name} saved!")
            st.rerun()

st.markdown("---")

# --- Filter & display recipes ---
if not recipes:
    st.info("No recipes yet. Add your first one above!")
else:
    col1, col2 = st.columns(2)
    with col1:
        filter_cuisine = st.selectbox("Filter by cuisine", ["All"] + list(set(r["cuisine"] for r in recipes)))
    with col2:
        filter_meal = st.selectbox("Filter by meal type", ["All", "Breakfast", "Lunch", "Dinner", "Snack"])

    filtered = recipes
    if filter_cuisine != "All":
        filtered = [r for r in filtered if r["cuisine"] == filter_cuisine]
    if filter_meal != "All":
        filtered = [r for r in filtered if filter_meal in r.get("meal_type", [])]

    st.markdown(f"**{len(filtered)} recipe(s) found**")
    st.markdown("---")

    for idx, recipe in enumerate(filtered):
        with st.expander(f"**{recipe['name']}** · {recipe['cuisine']} · {recipe['source_type']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Meal type:** {', '.join(recipe.get('meal_type', []))}")
                st.markdown(f"**Prep time:** {recipe.get('prep_time', 'N/A')}")
                if recipe.get("source_label"):
                    st.markdown(f"**Source:** {recipe['source_label']}")
                if recipe.get("source_url"):
                    st.markdown(f"[🔗 View original]({recipe['source_url']})")
            with col2:
                if recipe.get("notes"):
                    st.info(f"📝 {recipe['notes']}")

            st.markdown("**Ingredients:**")
            st.code(recipe.get("ingredients", ""), language=None)
            st.markdown("**Steps:**")
            st.write(recipe.get("steps", ""))

            col_edit, col_delete = st.columns(2)

            with col_delete:
                if st.button("🗑️ Delete recipe", key=f"del_recipe_{idx}"):
                    recipes.remove(recipe)
                    save_recipes(recipes)
                    st.rerun()

            with col_edit:
                if st.button("✏️ Edit recipe", key=f"edit_recipe_{idx}"):
                    st.session_state[f"editing_{idx}"] = True

            if st.session_state.get(f"editing_{idx}", False):
                new_name = st.text_input("Recipe name", value=recipe["name"], key=f"edit_name_{idx}")
                new_cuisine = st.selectbox("Cuisine", [
                    "Indian", "Italian", "Indo-Chinese", "Continental",
                    "Mexican", "Middle Eastern", "Other"
                ], index=["Indian", "Italian", "Indo-Chinese", "Continental",
                          "Mexican", "Middle Eastern", "Other"].index(recipe.get("cuisine", "Indian")),
                                           key=f"edit_cuisine_{idx}")
                new_ingredients = st.text_area("Ingredients", value=recipe.get("ingredients", ""),
                                               key=f"edit_ing_{idx}")
                new_steps = st.text_area("Steps", value=recipe.get("steps", ""), key=f"edit_steps_{idx}")
                new_notes = st.text_area("Notes", value=recipe.get("notes", ""), key=f"edit_notes_{idx}")

                if st.button("💾 Save changes", key=f"save_edit_{idx}"):
                    actual_idx = recipes.index(recipe)
                    recipes[actual_idx]["name"] = new_name
                    recipes[actual_idx]["cuisine"] = new_cuisine
                    recipes[actual_idx]["ingredients"] = new_ingredients
                    recipes[actual_idx]["steps"] = new_steps
                    recipes[actual_idx]["notes"] = new_notes
                    save_recipes(recipes)
                    st.session_state[f"editing_{idx}"] = False
                    st.success("✅ Recipe updated!")
                    st.rerun()