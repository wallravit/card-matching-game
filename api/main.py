from fastapi import FastAPI
from api.routes import users


def create_app() -> FastAPI:
    app = FastAPI(title="card-matching-game")

    app.include_router(users.router)
    return app
    