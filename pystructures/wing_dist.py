import numpy as np
from typing import Tuple


def CalcAverageCDist(b: float, CRoot: float, CTip: float, S: float) -> Tuple[np.ndarray, np.ndarray]:

    Lambda = CTip/CRoot
    y = np.linspace(0, b/2, 21)
    TrapCDist = CRoot*(1-(2*y/b)*(1-Lambda))            # Trapezoidal Chord Distribution
    EllipCDist = (4*S)/(np.pi*b)*(1-(2*y/b)**2)**0.5    # Elliptical Chord Distribution
    AverageCDist = (TrapCDist+EllipCDist)/2             # Average Chord Distribution

    return AverageCDist


def CalcAverageLDist(q: float, Cl_alpha: float, b: float, CRoot: float, CTip: float, S: float) -> Tuple[np.ndarray, np.ndarray]:

    cdist = CalcAverageCDist(b, CRoot, CTip, S)
    averageLDist = q * Cl_alpha * cdist            # Average Lift Distribution

    return averageLDist
