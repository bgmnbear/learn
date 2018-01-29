# Document string
def pressure(v, t, n):
    """Compute the pressure in pascals of an ideal gas.
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas
    """
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v


# Parameter default value
k_b = 1.38e-23


def pressure1(v, t, n=6.022e23):
    """Compute the pressure in pascals of an ideal gas.
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas (default: one mole)
    """
    return n * k_b * t / v


print('---Parameter default value---')
print(pressure1(1, 273.15))
