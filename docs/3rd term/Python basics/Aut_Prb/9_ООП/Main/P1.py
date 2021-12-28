def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
class Fraction:
    def __init__(self, numerator, denominator):
        d = abs(gcd(numerator, denominator))
        if numerator*denominator < 0:
            self.num = - abs(numerator // d)
            self.den = abs(denominator // d)
        elif denominator == 0:
            raise ZeroDivisionError
        else:
            self.num = abs(numerator // d)
            self.den = abs(denominator // d)
    
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + '/' + str(self.den)
    
    def __pos__(self):
        return Fraction(self.num, self.den)
    
    def __neg__(self):
        return Fraction(- self.num, self.den)
 
    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num*other.den + other.num*self.den, self.den*other.den)
        elif isinstance(other, int):
            return Fraction(self.num + other*self.den, self.den)
 
    def __radd__(self, other):
        return self + other
 
    def __sub__(self, other):
        return self + (-other)
 
    def __rsub__(self, other):
        return other + (-self)
 
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num*other.num, self.den*other.den) 
        else:
            return Fraction(self.num*other, self.den)
 
    def __rmul__(self, other):
        return self*other
 
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self * Fraction(other.den, other.num)
        else:
            return self*Fraction(1, other)
    
    def __rtruediv__(self, other):
        a = self / other
        return Fraction(a.den, a.num)
    
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return other.num == self.num and other.den == self.den
        else:
            return other == self.num and 1 == self.den
