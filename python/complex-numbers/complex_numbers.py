import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(
            real=self.real + other.real, imaginary=self.imaginary + other.imaginary
        )

    def __mul__(self, other):
        return ComplexNumber(
            real=self.real * other.real - self.imaginary * other.imaginary,
            imaginary=self.real * other.imaginary + self.imaginary * other.real,
        )

    def __sub__(self, other):
        return ComplexNumber(
            real=self.real - other.real, imaginary=self.imaginary - other.imaginary
        )

    def __truediv__(self, other):
        denom = abs(other) ** 2
        return ComplexNumber(
            real=(self.real * other.real + self.imaginary * other.imaginary) / denom,
            imaginary=(self.imaginary * other.real - self.real * other.imaginary)
            / denom,
        )

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(real=self.real, imaginary=-self.imaginary)

    def exp(self):
        scale = math.exp(self.real)
        return ComplexNumber(
            real=scale * math.cos(self.imaginary),
            imaginary=scale * math.sin(self.imaginary),
        )
