def mod_exponent(_base, _pow, _mod):
    res = 1  # Initialize result
    _base = _base % _mod  # Update base if it is more than or equal _mod
    while _pow > 0:
        if _pow & 1:  # if _pow is odd multiply it with result
            res = (res * _base) % _mod
        _pow = _pow >> 1  # _pow must be even now
        _base = (_base * _base) % _mod
    return res


if __name__ == '__main__':
    base = 2
    power = 5
    mod = 6
    print(mod_exponent(base, power, mod))
