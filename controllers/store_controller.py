from Models.store import Store
from fastapi import HTTPException, Depends, Cookie, status, APIRouter
from fastapi.responses import RedirectResponse
import json

router = APIRouter()

# File to store user data
STORE_DATA_FILE = "store_data.json"


# Helper function to load user data from JSON file
def load_store_data():
    try:
        with open(STORE_DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Helper function to save user data to JSON file
def save_store_data(data):
    with open(STORE_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# Endpoint for user sign-up
@router.post("/signup/")
async def signup(u: str, c: str, e: str, cat: str, p: str):

    store = Store(username=u, cnpj=c, email=e, categoria=cat, password=p)

    store_data = load_store_data()

    if store.cnpj in store_data:
        raise HTTPException(status_code=400, detail="CPNJ already registered")

    store_data[store.cnpj] = {"password": store.password}

    save_store_data(store_data)

    return {"message": "Admin signed up successfully"}


# Endpoint for user login
@router.post("/login/")
async def login(username: str, password: str):
    user_data = load_store_data()
    if username not in user_data or user_data[username]["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    response = RedirectResponse(url=f"/auth/{username}", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="username", value=username)
    return response

# Dependency to check if user is logged in
def get_current_user(username: str = Cookie(None)):
    user_data = load_store_data()
    if username not in user_data:
        raise HTTPException(status_code=401, detail="You must be logged in")
    return username

# página individual
@router.get("/auth/{user}")
async def user_page(user: str = Depends(get_current_user)):
    return {"message": f"Welcome, {user}!"}