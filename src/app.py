from fastapi import FastAPI

from api.v1 import router as api_v1


def _start_app() -> None:
    app = FastAPI()
    app.title = 'Currency Converter'

    app.include_router(api_v1.router)
    return(app)


app = _start_app()