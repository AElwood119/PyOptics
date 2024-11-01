"""A basic simulation of light reflecting off a mirror as the first sub-project of this
project."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
initial_angle = 30  # Angle of incidence in degrees
mirror_x = np.array([-1, 1])  # Mirror surface along the x-axis
mirror_y = np.array([0, 0])
