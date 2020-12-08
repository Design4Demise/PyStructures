import numpy as np
from typing import Union


torsion_coeff = {
    'width_thickness': [1.00, 1.50, 1.75, 2.00, 2.50, 3.00, 4, 6, 8, 10],
    'alpha': [0.208, 0.231, 0.239, 0.246, 0.258, 0.267, 0.282, 0.299, 0.307, 0.313],
    'beta': [0.141, 0.196, 0.214, 0.229, 0.249, 0.263, 0.281, 0.299, 0.307, 0.313]
}


def rect_shear_stress(torque: Union[np.ndarray, float],
                      width: Union[np.ndarray, float],
                      thickness: Union[np.ndarray, float]) -> Union[float, np.ndarray]:

    """Calculate Shear Stress for rectangle.

    Parameters
    ----------
    torque: Union[np.ndarray, float]
        Torques applied
    width: Union[np.ndarray, float]
        Width of beam
    thickness: Union[np.ndarray, float]
        Thickness of beam

    Returns
    -------
    shear_stress: Union[np.ndarray, float]
        Shear Stress in beam
    """

    # --> raymer :: eqn :: 14.49
    coeff_alpha = np.interp(width / thickness, torsion_coeff['width_thickness'], torsion_coeff['alpha'])
    shear_stress = torque / (coeff_alpha * width * thickness ** 2)

    return shear_stress


def rect_angular_twist(torque: Union[np.ndarray, float],
                       width: Union[np.ndarray, float],
                       thickness: Union[np.ndarray, float],
                       length: Union[np.ndarray, float],
                       shear_modulus: float) -> Union[np.ndarray, float]:

    """Calculate Angular Twist

    Parameters
    ----------
    torque: Union[np.ndarray, float]
        Torques applied
    width: Union[np.ndarray, float]
        Width of beam
    thickness: Union[np.ndarray, float]
        Thickness of beam
    length: Union[np.ndarray, float]
        Length of beam
    shear_modulus: float
        Shear Modulus of material

    Returns
    -------
    angular_twist: Union[np.ndarray, float]
        Twist of beam in radians
    """

    # --> raymer :: eqn :: 14.50
    coeff_beta = np.interp(width / thickness, torsion_coeff['width_thickness'], torsion_coeff['beta'])
    angular_twist = (torque * length) / (coeff_beta * width * (thickness ** 3) * shear_modulus)

    return angular_twist
