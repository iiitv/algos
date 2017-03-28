"""
Modular Exponential
"""

def mod_exponent(base, power, mod):
    """
    function returns the [base ^ pow] % mod
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
