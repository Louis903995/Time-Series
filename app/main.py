from fastapi import FastAPI
from app.routers import predictions

app = FastAPI(
    title="Prediction API",
    description="API de prolongation de séries temporelles",
    version="1.0.0",
)

app.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
