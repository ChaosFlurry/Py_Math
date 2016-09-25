from com.math.util import Math
from decimal import Decimal


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        self._numerator = numerator

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        self._denominator = denominator

    @staticmethod
    def value_of(n):
        return Fraction(n, 1)

    def to_str(self):
        if self.is_undefined():
            return "Undefined"
        elif self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    @staticmethod
    def equals(f1, f2):
        if (f1.simplify().numerator == f2.simplify().numerator
                and f2.simplify().denominator == f1.simplify().denominator):
            return True
        return False

    def to_float(self):
        return self.numerator / self.denominator

    def to_decimal(self):
        return Decimal(self.numerator) / Decimal(self.denominator)

    def simplify(self):
        numerator = self.numerator
        denominator = self.denominator
        gcd = Math.gcd(numerator, denominator)

        # Floor division to maintain precision when dividing by large numbers
        numerator //= gcd
        denominator //= gcd

        if denominator < 0:
            numerator *= -1
            denominator *= -1

        return Fraction(int(numerator), int(denominator))

    def is_undefined(self):
        if self.denominator == 0:
            return True
        return False

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator).simplify()

    def add_int(self, n):
        return Fraction(self.numerator + self.numerator * n,
                        self.denominator).simplify()

    def add_fraction(self, f):
        return Fraction(self.numerator * f.denominator +
                        f.numerator * self.denominator,
                        self.denominator * f.denominator).simplify()

    def subtract_int(self, n):
        return Fraction(self.numerator - self.numerator * n,
                        self.denominator).simplify()

    def subtract_fraction(self, f):
        return Fraction(self.numerator * f.denominator -
                        f.numerator * self.denominator,
                        self.denominator * f.denominator).simplify()

    def multiply_int(self, n):
        return Fraction(self.numerator * n, self.denominator).simplify()

    def multiply_fraction(self, f):
        return Fraction(self.numerator * f.numerator,
                        self.denominator * f.denominator).simplify()

    def divide_int(self, n):
        return Fraction(self.numerator, self.numerator * n).simplify()

    def divide_fraction(self, f):
        return Fraction(self.numerator * f.denominator,
                        self.denominator * f.numerator).simplify()

    def pow(self, n):
        return Fraction(self.simplify().numerator ** n,
                        self.simplify().denominator ** n).simplify()
