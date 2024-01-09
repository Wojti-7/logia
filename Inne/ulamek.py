# Can you create a simple Python program?
#
# Certainly! I'd be happy to help you with a simple Python program.
# Could you please specify what kind of program you have in mind or provide some requirements?
# That way, I can tailor the example to better suit your needs.
#
# Perhaps a class representing a fraction with numerator and denominator and an addition operation?
#
# Certainly! Here's a simple Python program that defines a Fraction class with a numerator,
# denominator, and an addition operation.
# This program defines a Fraction class with an __init__ method for initialization,
# an __add__ method for addition, and a __str__ method for a human-readable representation of the fraction.
# The _gcd method is a helper function to find the greatest common divisor.
# The example usage creates two fractions, adds them together, and prints the result.

class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Zero")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        gcd = self._gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // gcd, new_denominator // gcd)

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

# Test

a = Fraction(1, 2)
b = Fraction(3, 4)
c = a + b
print(f"{a} + {b} = {c}")

d = Fraction(1, 5)
e = Fraction(3, 7)
f = d.__add__(e)
print(f"{d.__str__()} + {e.__str__()} = {f.__str__()}")
