from app.models.timeseries import MesureTemporelle
from typing import List
from datetime import timedelta


def predict_extension(series: List[MesureTemporelle]) -> List[MesureTemporelle]:
    # Simple prolongation linéaire pour l'exemple
    if len(series) < 2:
        return []
    last, prev = series[-1], series[-2]
    delta_t = last.d - prev.d
    delta_v = last.v - prev.v
    next_point = MesureTemporelle(d=last.d + delta_t, v=last.v + delta_v)
    return [next_point]
