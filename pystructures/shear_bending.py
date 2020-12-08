import numpy as np


def shearforce(spanwise_loc: np.ndarray, lift_distribution: np.ndarray) -> np.ndarray:

    """Calculate Shear Force due to Bending

    Parameters
    ----------
    spanwise_loc: np.ndarray
        Discretisation of spanwise locations.
    lift_distribution: np.ndarray
        Lif distribution across span

    Returns
    -------
    vf: np.ndarray
        Shear Force due to Bending
    """

    if not spanwise_loc.shape[0] == lift_distribution.shape[0]:
        raise ValueError('Spanwise Distribution and Lift Distribution must have the same shape.')

    vf = np.zeros_like(spanwise_loc)
    for i in range(spanwise_loc.shape[0]):
        vf[i] = np.sum(lift_distribution) - np.sum(lift_distribution[0:i])

    return vf


def shearstress(spanwise_loc: np.ndarray,
                lift_distribution: np.ndarray,
                wing_thickness: float,
                widths: np.ndarray,
                iy: float) -> np.ndarray:

    """Calculate Shear Stress

    Parameters
    ----------
    spanwise_loc: np.ndarray
        Discretisation of spanwise locations.
    lift_distribution: np.ndarray
        Lif distribution across span
    wing_thickness: float
        Thickness of wing segment
    widths: np.ndarray
        Width at given spanwise location.
    iy: float
        Moment of Inertia, Iy, of geometry,

    Returns
    -------
    shear_stress_dist: np.ndarray
        Array of Shear Stress
    """

    shearf = shearforce(spanwise_loc, lift_distribution)
    discrete_z = np.linspace(0, 1, 11) * wing_thickness / 2

    # --> raymer :: eqn :: 14.36
    shear_stress_dist = np.empty((discrete_z.shape[0], shearf.shape[0]))
    for idx_f, force in enumerate(shearf):
        for idx_z, z in enumerate(discrete_z):
            shear_stress_dist[idx_z, idx_f] = ((force / (widths[idx_f] * iy))
                                               * (wing_thickness / 2 - z)
                                               * (((wing_thickness / 2) ** 2) / 2 - (z ** 2) / 2))

    return shear_stress_dist


def bendingmoment(spanwise_loc: np.ndarray, lift_distribution: np.ndarray) -> np.ndarray:

    """Calculate Bending Moment

    Parameters
    ----------
    spanwise_loc: np.ndarray
        Spanwise locations at which to calculate bending moment
    lift_distribution: np.ndarray
        Lift distribution along wing

    Returns
    -------
    bending_moment: np.ndarray
        Bending moment along wing
    """

    if not spanwise_loc.shape[0] == lift_distribution.shape[0]:
        raise ValueError('Spanwise Distribution and Lift Distribution must have the same shape.')

    bending_moment = np.zeros_like(spanwise_loc)
    for i in range(spanwise_loc.shape[0]):
        bending_moment[i] = np.sum(spanwise_loc * lift_distribution) - np.sum(spanwise_loc[:i] * lift_distribution[:i])

    return bending_moment


def bendingstress(spanwise_loc: np.ndarray,
                  lift_distribution: np.ndarray,
                  wing_thickness: float,
                  moment_of_inertia_y: float,
                  n_points: int = 11) -> np.ndarray:

    bendingm = bendingmoment(spanwise_loc, lift_distribution)
    discrete_z = np.linspace(0, 1, n_points) * wing_thickness / 2

    # --> raymer :: eqn :: 14.35
    bending_stress_dist = np.empty((discrete_z.shape[0], bendingm.shape[0]))
    for idx_m, moment in enumerate(bendingm):
        for idx_z, z in enumerate(discrete_z):
            bending_stress_dist[idx_z, idx_m] = moment * z / moment_of_inertia_y

    return bending_stress_dist
