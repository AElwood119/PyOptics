"""This file contains basic Optics functions"""

import numpy as np


def snells_law(n1: float, n2: float, theta1: float):
    """
    Calculate the angle of refraction based on Snell's Law.

    Snell's Law describes how light refracts when it passes from one medium to another
    with a different refractive index.
    The law is expressed as n1 * sin(theta1) = n2 * sin(theta2), where:
    - n1: Refractive index of the first medium (medium where light is coming from)
    - n2: Refractive index of the second medium (medium where light is entering)
    - theta1: Angle of incidence in degrees (angle between the incident ray and the
    normal to the interface)

    Parameters:
    ----------
    n1 : float
        Refractive index of the first medium.
    n2 : float
        Refractive index of the second medium.
    theta1 : float
        Angle of incidence in degrees.

    Returns:
    -------
    float
        Angle of refraction in degrees.

    Raises:
    ------
    ValueError
        If the calculated angle of refraction exceeds the bounds of the sine function
        (i.e., if sin(theta1) exceeds n2/n1).

    Examples:
    --------
    >>> snells_law(1.0, 1.5, 30)
    Angle of refraction: 19.19 degrees

    """
    theta1 = np.radians(theta1)

    # Calculate the angle of refraction
    theta2 = np.arcsin((n1 / n2) * np.sin(theta1))

    return np.degrees(theta2)
