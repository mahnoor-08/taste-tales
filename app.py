import streamlit as st
from utils.recipe_loader import load_recipes, get_recipe_by_id, filter_recipes
from utils.helpers import get_recipe_image, load_css

st.set_page_config(
    page_title="Taste Tales",
    page_icon="🍜",
    layout="wide",
)

load_css()

# ---------- Session state setup ----------
if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = None
if "favorites" not in st.session_state:
    st.session_state.favorites = set()

recipes = load_recipes()


def go_to_recipe(recipe_id):
    st.session_state.selected_recipe = recipe_id


def go_home():
    st.session_state.selected_recipe = None


def toggle_favorite(recipe_id):
    if recipe_id in st.session_state.favorites:
        st.session_state.favorites.remove(recipe_id)
    else:
        st.session_state.favorites.add(recipe_id)


# ================= DETAIL PAGE =================
if st.session_state.selected_recipe:
    recipe = get_recipe_by_id(recipes, st.session_state.selected_recipe)

    if recipe is None:
        st.warning("Recipe not found.")
        st.button("← Back to all recipes", on_click=go_home)
    else:
        st.button("← Back to all recipes", on_click=go_home)

        col1, col2 = st.columns([1, 1.3])

        with col1:
            img_url = get_recipe_image(recipe["image_query"], recipe["name"])
            st.image(img_url, use_container_width=True)

        with col2:
            st.title(recipe["name"])
            tag_class = "tag-pakistani" if recipe["cuisine"] == "Pakistani" else "tag-korean"
            st.markdown(
                f'<span class="cuisine-tag {tag_class}">{recipe["cuisine"]}</span> '
                f'<span class="cuisine-tag" style="background-color:#E8D8C3;color:#292522;">{recipe["category"]}</span>',
                unsafe_allow_html=True,
            )
            st.write("")
            m1, m2, m3 = st.columns(3)
            m1.metric("⏱ Prep", recipe["prep_time"])
            m2.metric("🔥 Cook", recipe["cook_time"])
            m3.metric("👥 Servings", recipe["servings"])

            is_fav = recipe["id"] in st.session_state.favorites
            fav_label = "♥ Saved" if is_fav else "♡ Save Recipe"
            st.button(fav_label, on_click=toggle_favorite, args=(recipe["id"],))

        st.markdown("---")

        c1, c2 = st.columns([1, 1.3])
        with c1:
            st.subheader("Ingredients")
            for ing in recipe["ingredients"]:
                st.markdown(f"- {ing}")

        with c2:
            st.subheader("Instructions")
            for i, step in enumerate(recipe["steps"], start=1):
                st.markdown(f"**{i}.** {step}")

# ================= HOME PAGE =================
else:
    st.markdown(
        "<h1 style='text-align:center;'>🍜 Taste Tales</h1>"
        "<p style='text-align:center;color:#7A284B;'>Recipes that tell a story</p>",
        unsafe_allow_html=True,
    )

    # ---------- Sidebar filters ----------
    st.sidebar.header("Filters")
    cuisine_filter = st.sidebar.radio("Cuisine", ["All", "Pakistani", "Korean"])

    categories = ["All"] + sorted({r["category"] for r in recipes})
    category_filter = st.sidebar.selectbox("Category", categories)

    show_favorites_only = st.sidebar.checkbox("❤️ Show favorites only")

    search_query = st.text_input("🔍 Search your favorite recipe...", "")

    filtered = filter_recipes(
        recipes,
        cuisine=cuisine_filter,
        category=category_filter,
        search_query=search_query,
    )

    if show_favorites_only:
        filtered = [r for r in filtered if r["id"] in st.session_state.favorites]

    if not filtered:
        st.info("No recipes found. Try a different search or filter.")

    # ---------- Recipe grid ----------
    cols_per_row = 4
    for i in range(0, len(filtered), cols_per_row):
        row_recipes = filtered[i : i + cols_per_row]
        cols = st.columns(cols_per_row)
        for col, recipe in zip(cols, row_recipes):
            with col:
                img_url = get_recipe_image(recipe["image_query"], recipe["name"])
                tag_class = "tag-pakistani" if recipe["cuisine"] == "Pakistani" else "tag-korean"
                is_fav = "♥" if recipe["id"] in st.session_state.favorites else ""

                st.markdown(
                    f"""
                    <div class="recipe-card">
                        <img src="{img_url}" />
                        <div class="recipe-title">{recipe['name']} {is_fav}</div>
                        <div class="recipe-meta">⏱ {recipe['prep_time']} · 👥 {recipe['servings']}</div>
                        <span class="cuisine-tag {tag_class}">{recipe['cuisine']}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.button("View Recipe", key=f"btn_{recipe['id']}", on_click=go_to_recipe, args=(recipe["id"],))
