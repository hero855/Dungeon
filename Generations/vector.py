from math import pi, sin, cos
from random import random, randint


def point(h, k, r=1):
    theta = random() * 2 * pi
    return h + cos(theta) * r, k + sin(theta) * r


class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return (self.x * other.x2) + (self.y * other.y2)

    def __rmul__(self, other):
        return (self.y * other.y2) + (self.x * other.x2)


class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return

    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __imul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __itruediv__(self, scalar):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __pos__(self):
        return Vector3(self.x, self.y, self.z)

    def __xor__(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3(cx, cy, cz)

    def __eq__(self, other):
        if (self.x, self.y, self.z) == (other.x, other.y, other.z):
            return True
        else:
            return False

    def cross(self, other):
        return self ^ other

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    # TODO: make dunder unpacking method
    # def __enter__(self, *_, **__):
    #     return self.x, self.y, self.z
