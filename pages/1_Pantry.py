import streamlit as st
import json
import os

PANTRY_FILE = "data/pantry.json"

def load_pantry():
    if not os.path.exists(PANTRY_FILE):
        return []
    with open(PANTRY_FILE, "r") as f:
        return json.load(f)

def save_pantry(items):
    os.makedirs("data", exist_ok=True)
    with open(PANTRY_FILE, "w") as f:
        json.dump(items, f, indent=2)

st.set_page_config(page_title="Pantry", page_icon="🥫", layout="wide")
st.title("🥫 Pantry")
st.caption("Track everything you have at home")
st.markdown("---")

items = load_pantry()

# --- Add new item ---
with st.expander("➕ Add new item", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        name = st.text_input("Item name", placeholder="e.g. Oats")
    with col2:
        quantity = st.number_input("Quantity", min_value=0.0, step=0.5)
    with col3:
        unit = st.selectbox("Unit", ["g", "kg", "ml", "L", "pcs", "cups", "tbsp", "tsp"])
    with col4:
        category = st.selectbox("Category", ["Grains & Pulses", "Vegetables", "Fruits", "Dairy", "Spices", "Oils & Condiments", "Snacks", "Beverages", "Other"])

    status = st.radio("Status", ["✅ In Stock", "⚠️ Low", "❌ Out"], horizontal=True)

    if st.button("Add to Pantry"):
        if name.strip() == "":
            st.warning("Please enter an item name.")
        else:
            items.append({
                "name": name.strip(),
                "quantity": quantity,
                "unit": unit,
                "category": category,
                "status": status
            })
            save_pantry(items)
            st.success(f"✅ {name} added!")
            st.rerun()

st.markdown("---")

# --- Display pantry ---
if not items:
    st.info("Your pantry is empty. Add your first item above!")
else:
    # Group by category
    categories = sorted(set(i["category"] for i in items))

    for cat in categories:
        cat_items = [i for i in items if i["category"] == cat]
        st.subheader(cat)

        for idx, item in enumerate(items):
            if item["category"] != cat:
                continue

            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 2, 1])
            with col1:
                st.write(item["name"])
            with col2:
                st.write(f"{item['quantity']} {item['unit']}")
            with col3:
                st.write(item["status"])
            with col4:
                new_status = st.selectbox(
                    "Update",
                    ["✅ In Stock", "⚠️ Low", "❌ Out"],
                    index=["✅ In Stock", "⚠️ Low", "❌ Out"].index(item["status"]),
                    key=f"status_{idx}",
                    label_visibility="collapsed"
                )
                if new_status != item["status"]:
                    items[idx]["status"] = new_status
                    save_pantry(items)
                    st.rerun()
            with col5:
                if st.button("🗑️", key=f"delete_{idx}"):
                    items.pop(idx)
                    save_pantry(items)
                    st.rerun()

        st.markdown("---")