import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY", "your_api_key")
SHOPIFY_API_SECRET = os.getenv("SHOPIFY_API_SECRET", "your_api_secret")

@app.get("/")
def read_root():
    return {"message": "Shopify Price Tracker B2B SaaS is running live!"}

@app.get("/auth/shopify")
def shopify_auth(shop: str):
    redirect_uri = "https://YOUR_RENDER_URL.onrender.com/auth/shopify/callback"
    scopes = "read_products,write_products"
    auth_url = f"https://{shop}/admin/oauth/authorize?client_id={SHOPIFY_API_KEY}&scope={scopes}&redirect_uri={redirect_uri}"
    return RedirectResponse(auth_url)

@app.get("/auth/shopify/callback")
def shopify_callback(shop: str, code: str):
    return {"status": "success", "shop": shop, "code": code}
