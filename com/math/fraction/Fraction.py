from com.math.util import MathUtil


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

    def simplify(self):
        numerator = self.numerator
        denominator = self.denominator
        gcd = MathUtil.gcd(numerator, denominator)

        numerator /= gcd
        denominator /= gcd

        if denominator < 0:
            numerator *= -1
            denominator *= -1
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def is_undefined(self):
        if self.denominator == 0:
            return True
        else:
            return False

a = Fraction(5, 6)
print(a.to_str())
g = Fraction.value_of(2)
f = g.to_str()
print(f)
