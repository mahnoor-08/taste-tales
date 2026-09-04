# 🍜 Taste Tales

Pakistani + Korean recipe discovery web app, built with Streamlit.

## 📁 Project Structure

```
taste-tales/
├── app.py                  # Main app
├── requirements.txt        # Python dependencies
├── data/
│   └── recipes.json        # All recipe data (add more recipes here!)
├── utils/
│   ├── recipe_loader.py    # Loads & filters recipes.json
│   └── helpers.py          # Image fetching (Unsplash) + CSS theme
└── .streamlit/
    ├── config.toml         # Color theme
    └── secrets.toml        # (you create this locally — NEVER commit it)
```

## 🖥️ Run it locally

1. Install Python 3.9+ if you don't have it.
2. Open a terminal in the `taste-tales` folder and install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional) To fetch real photos automatically, create a file
   `.streamlit/secrets.toml` with:
   ```
   UNSPLASH_ACCESS_KEY = "your_unsplash_key_here"
   ```
   Without this file, the app still works fine — it just shows a clean
   placeholder image instead of a fetched photo.
4. Run the app:
   ```
   streamlit run app.py
   ```
5. It opens automatically in your browser at `http://localhost:8501`.

## 🔑 Getting a free, permanent Unsplash API key

1. Go to https://unsplash.com/developers and create a free account.
2. Click **"Your apps" → "New Application"**.
3. Accept the API terms, give your app a name (e.g. "Taste Tales").
4. You'll get an **Access Key** — this does not expire on its own as long
   as you don't revoke it. Free ("Demo") tier allows 50 requests/hour,
   which resets every hour — plenty for personal browsing.
5. Never paste this key directly into `app.py` or any file you commit to
   GitHub — always use `secrets.toml` (see below).

## 🐙 Push to GitHub

1. Create a new repository on GitHub (e.g. `taste-tales`).
2. In the `taste-tales` folder, run:
   ```
   git init
   git add .
   git commit -m "Initial commit: Taste Tales recipe app"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/taste-tales.git
   git push -u origin main
   ```
3. Check on GitHub that `.streamlit/secrets.toml` did **NOT** get uploaded
   (it shouldn't — it's in `.gitignore`). If you don't have a secrets.toml
   locally yet, that's fine, it's optional.

## 🚀 Deploy on Streamlit Community Cloud

1. Go to https://share.streamlit.io and sign in with your GitHub account.
2. Click **"Create app"** → **"From existing repo"**.
3. Select your `taste-tales` repository, branch `main`, and main file `app.py`.
4. Click **"Advanced settings"** → **Secrets**, and paste (only if you got an Unsplash key):
   ```
   UNSPLASH_ACCESS_KEY = "your_unsplash_key_here"
   ```
5. Click **Deploy**. In a minute or two you'll get a live public link like
   `https://taste-tales.streamlit.app`.
6. To update the app later, just push new commits to GitHub — Streamlit
   Cloud redeploys automatically.

## ➕ Adding more recipes

Open `data/recipes.json` and add a new object following the same
structure as the existing ones (id, name, cuisine, category, image_query,
prep_time, cook_time, servings, ingredients, steps). No code changes
needed — the app reads this file automatically.

## 🗺️ What's built vs. what's next

**Already working:** recipe grid with cards, click-through detail pages,
search, cuisine/category filters, favorites (session-based), Unsplash
image fetching with safe fallback, custom aesthetic theme.

**Possible next steps:** persist favorites across sessions (e.g. using
`st.connection` with a small database), add more recipes, add a
YouTube/video link field per recipe, add more cuisines.
