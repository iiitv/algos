def mod_expo(base, power, mod):
    res = 1  # Initialize result
    base = base % mod  # Update base if it is more than or equal mod_
    while power > 0:
        if power & 1:  # if pow_ is odd multiply it with result
            res = (res * base) % mod
        power = power >> 1  # _pow must be even now
        base = (base * base) % mod
    return res


def main():
    base = int(input())
    power = int(input())
    mod = int(input())
    print(mod_expo(base, power, mod))


if __name__ == '__main__':
    main()

