"""Planejador básico de trajetória e comandos de movimento do Roboldo."""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Pose2D:
    x: float
    y: float
    theta: float = 0.0


def compute_distance(start: Pose2D, goal: Pose2D) -> Tuple[float, float]:
    """Retorna a distância euclidiana (dx, dy) entre duas poses no mapa."""
    return (goal.x - start.x, goal.y - start.y)
