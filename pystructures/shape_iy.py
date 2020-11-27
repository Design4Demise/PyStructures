import numpy as np


def calc_rect_shape_iy(width: float, height: float, internal_width: float = 0, internal_height: float = 0) -> float:

    rect_moment_of_inertia_y = ((height * width ** 3) - (internal_height * internal_width ** 3)) / 12

    return rect_moment_of_inertia_y


def calc_circ_shape_iy(external_radius: float, internal_radius: float = 0) -> float:

    circ_moment_of_inertia_y = (np.pi * (external_radius ** 4 - internal_radius ** 4) / 4)

    return circ_moment_of_inertia_y
