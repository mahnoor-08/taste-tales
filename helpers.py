import streamlit as st
import requests

PLACEHOLDER_BASE = "https://placehold.co/600x400"


@st.cache_data(show_spinner=False)
def get_recipe_image(query: str, recipe_name: str = "") -> str:
    """
    Fetch a recipe image URL from Unsplash based on the query.
    Falls back to a clean placeholder image if no API key is configured
    or if the request fails, so the app NEVER crashes because of images.
    """
    access_key = st.secrets.get("UNSPLASH_ACCESS_KEY", None)

    if access_key:
        try:
            response = requests.get(
                "https://api.unsplash.com/search/photos",
                params={"query": query, "per_page": 1, "orientation": "landscape"},
                headers={"Authorization": f"Client-ID {access_key}"},
                timeout=5,
            )
            if response.status_code == 200:
                results = response.json().get("results", [])
                if results:
                    return results[0]["urls"]["regular"]
        except requests.RequestException:
            pass  # fall through to placeholder

    # Fallback: a clean placeholder with the recipe name on it
    safe_text = (recipe_name or query).replace(" ", "+")
    return f"{PLACEHOLDER_BASE}/F7F3EC/7A284B?text={safe_text}"


def load_css():
    """Injects the 'Saffron Seoul' aesthetic theme as custom CSS."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Poppins:wght@300;400;500;600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
        }

        .stApp {
            background-color: #F7F3EC;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            color: #7A284B;
        }

        .recipe-card {
            background-color: #FFFDF8;
            border-radius: 16px;
            padding: 12px;
            box-shadow: 0 2px 10px rgba(41, 37, 34, 0.08);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            margin-bottom: 20px;
            border: 1px solid #E8D8C3;
        }

        .recipe-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(122, 40, 75, 0.15);
        }

        .recipe-card img {
            border-radius: 12px;
            width: 100%;
            height: 180px;
            object-fit: cover;
        }

        .recipe-title {
            font-weight: 600;
            font-size: 17px;
            color: #292522;
            margin-top: 8px;
        }

        .recipe-meta {
            color: #7A284B;
            font-size: 13px;
            margin-top: 2px;
        }

        .cuisine-tag {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
            margin-top: 6px;
        }

        .tag-pakistani {
            background-color: #E8D8C3;
            color: #7A284B;
        }

        .tag-korean {
            background-color: #DDE5DC;
            color: #4A5C4C;
        }

        div.stButton > button {
            background-color: #7A284B;
            color: #FFFDF8;
            border-radius: 20px;
            border: none;
            padding: 6px 20px;
            font-weight: 500;
        }

        div.stButton > button:hover {
            background-color: #5E1E3A;
            color: #FFFDF8;
        }

        section[data-testid="stSidebar"] {
            background-color: #FFFDF8;
            border-right: 1px solid #E8D8C3;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
