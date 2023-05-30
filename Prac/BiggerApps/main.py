# Using background tasks
from fastapi import Depends, FastAPI, BackgroundTasks

from dependencies import get_query_token, get_token_header
from internal import admin
from routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
        admin.router,
        prefix="/admin",
        tags=["admin"],
        dependencies=[Depends(get_token_header)],
        responses={418: {"description": "I'm a teapot"}},
)

def write_notifications(email: str, message = ""):
    with open("notifications.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
