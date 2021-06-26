from __future__ import division


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

class Rational:
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(numer=self.numer * other.denom + other.numer * self.denom, denom=self.denom * other.denom)

    def __sub__(self, other):
        return Rational(numer=self.numer * other.denom - other.numer * self.denom, denom=self.denom * other.denom)

    def __mul__(self, other):
        return Rational(numer=self.numer * other.numer, denom=self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(numer=self.numer * other.denom, denom=self.denom * other.numer)

    def __abs__(self):
        return Rational(numer=abs(self.numer), denom=abs(self.denom))

    def __pow__(self, power):
        return Rational(numer=self.numer ** power, denom=self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
