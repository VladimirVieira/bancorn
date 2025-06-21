from fastapi import FastAPI

from controller.conta_controller import router

app = FastAPI(
    title="BancoRN API",
    description="Sistema bancário simples com API REST",
)

app.include_router(router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
