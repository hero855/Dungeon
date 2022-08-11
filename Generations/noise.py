from opensimplex import OpenSimplex

gen = OpenSimplex()


def simple_curve(value):
    start = 0.4
    end = 0.6
    if value < start:
        return 0.0
    if value > end:
        return 1.0
    return (value - start) * (1 / (end - start))


def plains(x, y):
    value = (gen.noise2d(x, y))
    value = value**0.25
    value = value - 0.6
    return value


def mountains(x, y):
    value = gen.noise2d(x * 6.0, y * 3.0)
    return value * 2.0


def combined(x, y):
    m = mountains(x, y)
    p = plains(x, y)
    w = simple_curve(x, y)
    return (p * w) + (m * (1 - w))

