import numpy as np


def schrenks_chord_dist(wing_span: float,
                        root_chord: float,
                        tip_chord: float,
                        wing_area: float,
                        n_points: int = 21) -> np.ndarray:

    """Calculate Chord Distribution - Schrenk's Approximation.

    Parameters
    ----------
    wing_span: float
        Wing span
    root_chord: float
        Length of the chord at the root
    tip_chord:
        Length of the chord at the tip
    wing_area: float
        Area of the wing
    n_points: int
        Number of points to use in discretisation

    Returns
    -------
    schrenks_dist: np.ndarray
        Chord Distribution
    """

    lamb_da = tip_chord / root_chord
    span_loc = np.linspace(0, wing_span / 2, n_points)

    # --> raymer :: eqn :: 14.9
    trapezoidal_dist = root_chord * (1 - (2 * span_loc / wing_span) * (1 - lamb_da))

    # --> raymer :: eqn :: 14.11
    eliptical_dist = (4 * wing_area) / (np.pi * wing_span) * np.sqrt(1 - (2 * span_loc / wing_span) ** 2)

    # average chord distribution - schrenks approximation
    schrenks_dist = (trapezoidal_dist + eliptical_dist ) / 2
    
    return schrenks_dist


def schrenks_lift_dist(q: float,
                       cl: float,
                       wing_span: float,
                       root_chord: float,
                       tip_chord: float,
                       wing_area: float,
                       n_points: int = 21) -> np.ndarray:

    """Calculate Lift Distribution According to Schrenk's Approximation

    Parameters
    ----------
    q: float
        Dynamic Pressure
    cl: float
        Lift Curve Slope
    wing_span: float
        Wing span
    root_chord: float
        Length of the chord at the root
    tip_chord:
        Length of the chord at the tip
    wing_area: float
        Area of the wing
    n_points: int
        Number of points to use in discretisation

    Returns
    -------
    schrenks_lift_dist: np.ndarray
        Lift Distribution
    """

    c_dist = schrenks_chord_dist(wing_span, root_chord, tip_chord, wing_area, n_points)
    schrenks_lift_dist = q * cl * c_dist

    return schrenks_lift_dist
