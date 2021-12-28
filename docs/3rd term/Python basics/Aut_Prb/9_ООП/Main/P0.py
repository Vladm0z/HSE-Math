def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n


class Fraction:
    def __init__(self, numerator, denominator):
        self.num = int(numerator / gcd(abs(numerator), abs(denominator)))
        self.denom = int(denominator / gcd(abs(numerator), abs(denominator)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        elif self.denom == 0:
            raise ZeroDivisionError
    
    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return '%s/%s' %(self[0], -1*self[1])
            else:
                return '%s/%s' %(self[0], self[1])
        elif self.denom == 1:
            return str(self.num)
        else:
            return '%s/%s' %(self.num, self.denom)
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return -self.num, self.denom
    
    def __eq__(self, other):
        return self.num*other.num == self.denom*other.denom
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            self.num = int((self.num*other.denom + self.denom*other.num)/
                        (gcd(abs(self.num*other.denom + self.denom*other.num),abs(self.denom*other.denom))))
            self.denom = int((self.denom*other.denom)/
                        (gcd(abs(self.num*other.denom + self.denom*other.num),abs(self.denom*other.denom))))
        elif isinstance(other, int):
            self.num = int((self.num + self.denom*other)/
                        (gcd(abs(self.num + self.denom*other),abs(self.denom))))
            self.denom = int(self.denom/
                        (gcd(abs(self.num + self.denom*other),abs(self.denom))))
        return self

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        return self.num*other.denom - self.denom*other.num, self.denom*other.denom
    
    def __mul__(self, other):
        return self.num*other.num, self.denom*other.denom
    
    def __div__(self, other):
        return self.num*other.denom, self.denom*other.num
