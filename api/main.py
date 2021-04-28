from fastapi import FastAPI

from api.routes import user_router


def create_app() -> FastAPI:
    app = FastAPI(title="card-matching-game")

    app.include_router(user_router)
    return app
