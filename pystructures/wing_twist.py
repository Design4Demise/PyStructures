import numpy as np


coeff_width_thickness_ratio_ref = [1.00, 1.50, 1.75, 2.00, 2.50, 3.00, 4, 6, 8, 10]
coeff_alpha_ref = [0.208, 0.231, 0.239, 0.246, 0.258, 0.267, 0.282, 0.299, 0.307, 0.313]
coeff_beta_ref = [0.141, 0.196, 0.214, 0.229, 0.249, 0.263, 0.281, 0.299, 0.307, 0.313]


def rect_shear_stress(torque: np.ndarray, width: np.ndarray, thickness: np.ndarray) -> np.ndarray:

    coeff_alpha = np.interp(width / thickness, coeff_width_thickness_ratio_ref, coeff_alpha_ref)
    shear_stress = torque / (coeff_alpha * width * thickness ** 2)

    return shear_stress


def rect_angular_twist(torque: np.ndarray,
                       length: float,
                       shear_modulus: float,
                       width: np.ndarray,
                       thickness: np.ndarray) -> np.ndarray:

    coeff_beta = np.interp(width / thickness, coeff_width_thickness_ratio_ref, coeff_beta_ref)
    angular_twist = (torque * length) / (coeff_beta * width * (thickness ** 3) * shear_modulus)

    return angular_twist
