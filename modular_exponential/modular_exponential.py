"""
Modular Exponential
"""


def mod_exponent(base, power, mod):
    """
    Modular exponential of a number

    :param base : number which is going to be raised
    :param power : power to which the number is raised
    :param mod   : number by modulo has to be performed

    :return : number raised to power and modulo by mod [(base ^ power) % mod]
    """
    res = 1  # Initialize result
    base = base % mod  # Update base if it is more than or equal mod_
    while power > 0:
        if power & 1:  # if pow_ is odd multiply it with result
            res = (res * base) % mod
        power = power >> 1  # _pow must be even now
        base = (base * base) % mod
    return res


def main():
    """
    Driver function
    """
    base = 42
    power = 58
    mod = 69
    print(mod_exponent(base, power, mod))


if __name__ == '__main__':
    main()
