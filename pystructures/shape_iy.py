import numpy as np


def rect_iy(width: float,
            height: float,
            internal_width: float = 0.0,
            internal_height: float = 0.0) -> float:

    """Calculate Moment of Inertia, Iy, for Rectangle.

    Parameters
    ----------
    width: float
        Width of rectangle
    height: float
        Height of rectangle
    internal_width: float
        Internal width of rectangle
    internal_height: float
        Internal height of rectangle

    Returns
    -------
    float
        Moment of Inertia (Iy) of Rectangle
    """

    if not (internal_height < height) and (internal_width < width):
        raise ValueError('Inner dimensions must be smaller than outer dimensions.')

    return ((height * width ** 3) - (internal_height * internal_width ** 3)) / 12


def circ_iy(radius: float, internal_radius: float = 0.0) -> float:

    """Calculate Moment of Inertia, Iy, for Circle.

    Parameters
    ----------
    radius: float
        Radius of circle
    internal_radius: float
        Internal radius of circle

    Returns
    -------
    float
        Moment of Inertia, Iy, of Circle
    """

    if not internal_radius < radius:
        raise ValueError('Inner radius must be smaller than external radius.')

    return np.pi * (radius ** 4 - internal_radius ** 4) / 4
