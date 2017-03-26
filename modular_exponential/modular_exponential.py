def mod_exponent(base_, pow_, mod_):
    res = 1  # Initialize result
    base_ = base_ % mod_  # Update base if it is more than or equal mod_
    while pow_ > 0:
        if pow_ & 1:  # if pow_ is odd multiply it with result
            res = (res * base_) % mod_
        pow_ = pow_ >> 1  # _pow must be even now
        base_ = (base_ * base_) % mod_
    return res


if __name__ == '__main__':
    base = int(input())
    power = int(input())
    mod = int(input())
    print(mod_exponent(base, power, mod))

