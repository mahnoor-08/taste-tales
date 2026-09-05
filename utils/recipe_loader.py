import json
import os
import streamlit as st

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "recipes.json")


@st.cache_data
def load_recipes():
    """Load all recipes from the local JSON database."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        recipes = json.load(f)
    return recipes


def get_recipe_by_id(recipes, recipe_id):
    """Find a single recipe by its id."""
    for r in recipes:
        if r["id"] == recipe_id:
            return r
    return None


def filter_recipes(recipes, cuisine=None, category=None, search_query=None):
    """Filter recipes by cuisine, category, and/or a text search on the name."""
    filtered = recipes

    if cuisine and cuisine != "All":
        filtered = [r for r in filtered if r["cuisine"] == cuisine]

    if category and category != "All":
        filtered = [r for r in filtered if r["category"] == category]

    if search_query:
        q = search_query.strip().lower()
        filtered = [r for r in filtered if q in r["name"].lower()]

    return filtered
