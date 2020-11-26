import numpy as np
from typing import Tuple


def calc_average_c_dist(wing_span: float,
                        root_chord: float,
                        tip_chord: float,
                        wing_area: float,
                        n_points: int = 21) -> np.ndarray:

    lamb_da = tip_chord / root_chord
    y = np.linspace(0, wing_span / 2, n_points)
    trap_c_dist = root_chord * (1 - (2 * y / wing_span) * (1 - lamb_da))                            # Trapezoidal Chord Distribution
    ellip_c_dist = (4 * wing_area) / (np.pi * wing_span) * (1 - (2 * y / wing_span) ** 2) ** 0.5    # Elliptical Chord Distribution
    average_c_dist = (trap_c_dist+ellip_c_dist)/2                                                   # Average Chord Distribution

    return average_c_dist


def calc_average_l_dist(q: float,
                        cl_alpha: float,
                        wing_span: float,
                        root_chord: float,
                        tip_chord: float,
                        wing_area: float,
                        n_points: int = 21) -> np.ndarray:

    c_dist = calc_average_c_dist(wing_span, root_chord, tip_chord, wing_area, n_points)
    average_l_dist = q * cl_alpha * c_dist            # Average Lift Distribution

    return average_l_dist
