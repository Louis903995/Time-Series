from fastapi import APIRouter
from typing import List
from app.models.timeseries import MesureTemporelle
from app.services.prediction_service import predict_extension

router = APIRouter()


@router.post("/", response_model=List[MesureTemporelle])
async def get_prediction(series: List[MesureTemporelle]):
    """
    Prédit la prolongation d'une série temporelle.
    """
    return predict_extension(series)
