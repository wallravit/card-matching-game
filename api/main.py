from fastapi import FastAPI

from api.routes import game_router, root_router, user_router


def create_app() -> FastAPI:
    app = FastAPI(title="card-matching-game")

    app.include_router(root_router)
    app.include_router(user_router)
    app.include_router(game_router)
    return app
