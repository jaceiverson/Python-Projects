import uvicorn
from fastapi import FastAPI


def build_app():
    # initialize the FastAPI app
    app = FastAPI(
        title="Jace's API",
        version="0.1.0",
        summary="summary",
        description="decs",
        openapi_tags=[
            {
                "name": "Testing",
                "description": "tag",
            }
        ],
    )

    # import routers here
    from apis.test_apis import router as testing

    # include routers here
    app.include_router(testing, prefix="/test", tags=["Testing"])

    return app


def launch_app(app: FastAPI = build_app, host: str = "0.0.0.0", port: int = 8000):
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(build_app(), host="0.0.0.0", port=8000)
