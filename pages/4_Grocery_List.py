import streamlit as st
import json
import os
from utils.theme import apply_theme, page_header

MEAL_PLAN_FILE = "data/meal_plan.json"
RECIPES_FILE = "data/recipes.json"
PANTRY_FILE = "data/pantry.json"
GROCERY_FILE = "data/grocery.json"

def load_json(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

def save_json(filepath, data):
    os.makedirs("data", exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

st.set_page_config(page_title="Grocery List", page_icon="🛒", layout="wide")
apply_theme()
page_header("🛒", "Grocery List", "Auto-generated from your meal plan and pantry")

meal_plan = load_json(MEAL_PLAN_FILE)
recipes = load_json(RECIPES_FILE)
pantry = load_json(PANTRY_FILE)
grocery = load_json(GROCERY_FILE)

# Build a lookup for recipes
recipe_lookup = {r["name"]: r for r in recipes}

# Build pantry lookup — items in stock are available
pantry_in_stock = set(
    item["name"].lower() for item in pantry
    if item["status"] == "✅ In Stock"
)
pantry_low = set(
    item["name"].lower() for item in pantry
    if item["status"] == "⚠️ Low"
)

# --- Generate grocery list from meal plan ---
if st.button("🔄 Generate from this week's meal plan", type="primary"):
    needed = {}

    for entry in meal_plan:
        recipe_name = entry.get("recipe", "-- None --")
        if recipe_name == "-- None --":
            continue
        recipe = recipe_lookup.get(recipe_name)
        if not recipe:
            continue
        ingredients = recipe.get("ingredients", "").strip().split("\n")
        for ingredient in ingredients:
            ingredient = ingredient.strip()
            if not ingredient:
                continue
            key = ingredient.lower()
            if key not in needed:
                needed[key] = {
                    "name": ingredient,
                    "recipes": [],
                    "checked": False
                }
            if recipe_name not in needed[key]["recipes"]:
                needed[key]["recipes"].append(recipe_name)

    # Mark items already in stock
    grocery_list = []
    for key, item in needed.items():
        in_pantry = any(p in key for p in pantry_in_stock)
        is_low = any(p in key for p in pantry_low)
        status = "✅ Have it" if in_pantry else ("⚠️ Running low" if is_low else "🛒 Need to buy")
        grocery_list.append({
            "name": item["name"],
            "recipes": item["recipes"],
            "status": status,
            "checked": False
        })

    # Sort: need to buy first, then low, then have it
    order = {"🛒 Need to buy": 0, "⚠️ Running low": 1, "✅ Have it": 2}
    grocery_list.sort(key=lambda x: order.get(x["status"], 3))

    save_json(GROCERY_FILE, grocery_list)
    st.success(f"✅ Grocery list generated with {len(grocery_list)} items!")
    st.rerun()

st.markdown("---")

# --- Display grocery list ---
if not grocery:
    st.info("No grocery list yet. Click the button above to generate one from your meal plan!")
else:
    # Summary
    need_to_buy = [i for i in grocery if i["status"] == "🛒 Need to buy"]
    running_low = [i for i in grocery if i["status"] == "⚠️ Running low"]
    have_it = [i for i in grocery if i["status"] == "✅ Have it"]

    col1, col2, col3 = st.columns(3)
    col1.metric("🛒 Need to buy", len(need_to_buy))
    col2.metric("⚠️ Running low", len(running_low))
    col3.metric("✅ Already have", len(have_it))

    st.markdown("---")

    # Display each group
    for group_label, group_items in [
        ("🛒 Need to buy", need_to_buy),
        ("⚠️ Running low", running_low),
        ("✅ Already have", have_it)
    ]:
        if not group_items:
            continue

        st.markdown(f"### {group_label}")

        for idx, item in enumerate(grocery):
            if item["status"] != group_items[0]["status"] if group_items else True:
                pass
            if item["status"] != group_label.split(" — ")[0] and item not in group_items:
                continue
            if item not in group_items:
                continue

            col1, col2, col3 = st.columns([0.5, 3, 3])
            with col1:
                checked = st.checkbox(
                    "",
                    value=item.get("checked", False),
                    key=f"check_{idx}"
                )
                if checked != item.get("checked", False):
                    grocery[idx]["checked"] = checked
                    save_json(GROCERY_FILE, grocery)
                    st.rerun()
            with col2:
                name_style = "~~" if item.get("checked") else ""
                st.markdown(f"{name_style}{item['name']}{name_style}")
            with col3:
                recipes_used = ", ".join(item.get("recipes", []))
                st.caption(f"For: {recipes_used}")

        st.markdown("---")

    # Extra items
    st.markdown("### ➕ Add extra item")
    col1, col2 = st.columns([3, 1])
    with col1:
        extra_item = st.text_input("Item name", placeholder="e.g. Milk", label_visibility="collapsed")
    with col2:
        if st.button("Add"):
            if extra_item.strip():
                grocery.append({
                    "name": extra_item.strip(),
                    "recipes": ["Manual"],
                    "status": "🛒 Need to buy",
                    "checked": False
                })
                save_json(GROCERY_FILE, grocery)
                st.success(f"Added {extra_item}!")
                st.rerun()