import random
import time


def readPowerSim():
    """Simulates reading power from a power meter.

    Returns:
        float: A simulated power reading in milliwatts (mW).
    """

    base_power = 10.0  # Base power level in mW
    noise = random.uniform(-0.5, 0.5)
    simulated_reading = round(base_power + noise, 3)

    return simulated_reading
