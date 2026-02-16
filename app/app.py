"""
Sample API
"""

from fastapi import FastAPI
from model import User

from pprint import pprint

app = FastAPI()


# Routing
@app.get("/")
def root():
    return {"message": "hello friend 🌐"}


@app.get("/users/{uname}")
def fetch_user(uname: str, q: str | None = None):
    return {"uname": uname, "query": q}


@app.post("/signup/")
def create_user(user: User):
    pprint(user)
    return {"created": user, "status": "success"}


@app.get("/greet/{uname}")
def greet_user(uname: str):
    return {"message": f"Hello, {uname}! 👋"}
