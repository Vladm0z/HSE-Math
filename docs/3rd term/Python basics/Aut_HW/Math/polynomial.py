"""Polynomial"""

# tests
# init_open https://contest.yandex.ru/contest/29819/run-report/59267822/
# eq_open https://contest.yandex.ru/contest/29819/run-report/59268328/
# add_open https://contest.yandex.ru/contest/29819/run-report/59268388/
# der_open https://contest.yandex.ru/contest/29819/run-report/59268435/
# deg_open https://contest.yandex.ru/contest/29819/run-report/59268502/
# sub_open https://contest.yandex.ru/contest/29819/run-report/59268551/
# call_open https://contest.yandex.ru/contest/29819/run-report/59268698/
# mul_open https://contest.yandex.ru/contest/29819/run-report/59268755/
# iter_open https://contest.yandex.ru/contest/29819/run-report/59268866/
# real_poly_open https://contest.yandex.ru/contest/29819/run-report/59268913/
# 2pts_closed https://contest.yandex.ru/contest/29819/run-report/59267504/
# 4pts_closed https://contest.yandex.ru/contest/29819/run-report/59267679/
# 5pts_closed https://contest.yandex.ru/contest/29819/run-report/59267704/
# gcd


class Polynomial:
    # Initialize Polynomial
    def __init__(self, *coefficients):
        # using list [1, 2, 3] := 3x^2 + 2x + 1
        if isinstance(coefficients[0], list):
            self.coefficients = coefficients[0]
        # using dict {0:1, 1:2, 2:3} := 3x^2 + 2x + 1
        elif isinstance(coefficients[0], dict):
            self.coefficients = [0] * (max(coefficients[0].keys()) + 1)
            for (k, v) in coefficients[0].items():
                self.coefficients[k] = v
        # copy other Polynomial
        elif isinstance(coefficients[0], Polynomial):
            self.coefficients = coefficients[0].coefficients
            self.coefficients = self.coefficients[::-1]
        # ust bunch of coefficients
        else:
            self.coefficients = list(coefficients)
        # pop 0
        while (self.coefficients[len(self.coefficients) - 1] == 0)\
                and len(self.coefficients) > 1:
            (self.coefficients).pop(len(self.coefficients) - 1)
        self.coefficients = self.coefficients[::-1]

    def __repr__(self):
        return "Polynomial " + str(self.coefficients[::-1])

    # Fancy string
    def __str__(self):
        # Correct degree for each monomial
        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x "
            else:
                res = "x^" + str(degree) + " "
            return res

        degree = len(self.coefficients) - 1
        res = ""
        # for each monomial of polynomial
        for i in range(0, degree+1):
            coeff = self.coefficients[i]
            # coefficints in case of abs(coeff) = 1
            if abs(coeff) == 1 and i < degree:
                res += "{A}{B}".format(A=('+ ' if coeff > 0 else '- '),
                                       B=(x_expr(degree-i)))
            # other nonzero cases
            elif coeff != 0:
                res += "{A}{B}".format(A=('+ ' + str(coeff) if coeff > 0
                                          else '- ' + str(abs(coeff))),
                                       B=x_expr(degree-i))
        # delete first + sign
        res = res.lstrip('+')
        if res == '':
            return '0'
        elif res[0] == '-':
            res = '-'+res.lstrip('-').strip()
        return res.strip()

    # All polynomials are equal but some are more equal than others
    def __eq__(self, other):
        c1 = self.coefficients
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        else:
            c2 = Polynomial(other)
            return self.coefficients == c2.coefficients

    # Addition
    def __add__(self, other):
        c1 = self.coefficients[::-1]
        # sum of 2 polinomials
        if isinstance(other, Polynomial):
            c2 = other.coefficients[::-1]
            res = ([coeff1 + coeff2 for coeff1, coeff2 in zip(c1, c2)]
                   + (c1 if len(c1) > len(c2) else c2)[min(len(c1), len(c2)):])
        else:
            c1[0] += other
            res = c1
        return Polynomial(*res)

    # R addition
    def __radd__(self, other):
        # sum of polynomial and number
        return self+other

    # Negation
    def __neg__(self):
        # -coeff for each monomial
        return Polynomial(([-coef for coef in self.coefficients])[::-1])

    # Subtraction
    def __sub__(self, other):
        # = addition of neg polynomial
        return self + (-other)

    # R Subtraction
    def __rsub__(self, other):
        # = addition to neg polynomial
        return other + (-self)

    # Value at point
    def __call__(self, x):
        res = 0
        # sum of results for each monomial
        for coef in self.coefficients:
            res = res * x + coef
        return res

    # Degree of the polynomial
    def degree(self):
        return len(self.coefficients) - 1

    # Derivative
    def der(self, d=1):
        res = []
        exp = 1
        # return 0 if deg(polynomial) < d
        if self.degree() < d:
            return Polynomial(0)
        # exp = n*(n-1)*...*(n-d+1)
        for i in range(d):
            exp *= len(self.coefficients) - i - 1

        # find derivative for each monomial
        for i in range(len(self.coefficients) - d):
            res.append(int(self.coefficients[i] * exp))
            if exp != 1:
                exp *= ((len(self.coefficients) - i - d - 1) /
                        (len(self.coefficients) - i - 1))
        return Polynomial(*res[::-1])

    # Multiplication
    def __mul__(self, other):
        c1 = self.coefficients
        # Multiplication of 2 polynomials
        if isinstance(other, Polynomial):
            c2 = other.coefficients
            # length of result
            res = [0]*(len(c1)+len(c2)-1)
            # for power, coeff of self
            for self_power, self_coef in enumerate(c1):
                # for power, coeff of other
                for other_power, other_coef in enumerate(c2):
                    # add product of coefficients
                    # to monomial degree self_power + other_power
                    res[self_power + other_power] += self_coef * other_coef
            res = res[::-1]
        # Multiplication of polynomial and number
        else:
            res = ([c1[i]*other for i in range(len(self.coefficients))])[::-1]
        return Polynomial(*res)

    # R Multiplication
    def __rmul__(self, other):
        return self * other

    # mod
    def __mod__(self, other):
        c = self
        while c != 0 and c.degree() >= other.degree():
            a = c.coefficients[c.degree()]
            b = other.coefficients[other.degree()]
            t = a / b * Polynomial({c.degree()-other.degree(): 1})
            c -= t * other
        return с


    # Greatest Common Divisor
    def gcd(self, other):

        def gcd_R(с1, с2):
            с = с1 % с2
            if с == 0:
                return с2
            else:
                return gcd_R(с1, с2)
            
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        с = gcd_R(self, other)
        if с.degree() == 0:
            return 1
        else:
            a = gcd_of_n_numbers(c.coefficients)
            c.coefficients = [int(c.coefficients[i] / a) for i in range(len(c.coefficients))]
            return c

    # Iterator
    def __iter__(self):
        self.n = 0
        self.coefficients = self.coefficients[::-1]
        return self

    def __next__(self):
        if self.n <= len(self.coefficients) - 1:
            res = self.coefficients[self.n]
            self.n += 1
            return (self.n - 1, res)
        else:
            raise StopIteration

    # Monic polinomial
    def monic(self):
        c1 = [coef/self.coefficients[0] for coef in self.coefficients]
        for coef in range(len(c1)):
            if int(c1[coef]) == float(c1[coef]):
                c1[coef] = int(c1[coef])
        return Polynomial(c1[::-1])


# Exceptions

# Not Odd Degree (some of the even degree polynomials have no roots)
class NotOddDegreeException(Exception):
    def __init__(self, number, message='which is not odd'):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        out = ('Power of the given polynomial is'
               + self.number
               + ', '
               + self.message)
        return out


# Quadratic polynomial can't have degree large than 2
class DegreeIsTooBigException(Exception):
    def __init__(self, number, message='which is more than 2'):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        out = ('Power of the given polynomial is'
               + self.number
               + ', '
               + self.message)
        return out


# Find Real Roots of Odd Degree Polynomial
# using binomial method
class RealPolynomial(Polynomial):
    def __init__(self, coefficients):
        super().__init__(coefficients)
        # Exception
        if super().degree() % 2 == 0:
            raise NotOddDegreeException(super().degree())

    # finding root
    def find_root(self, eps=1.e-8):
        # let's work with monic polynomial cause it looks nice
        monic_poly = self.monic()
        right_arg = abs(monic_poly.degree() * min(monic_poly.coefficients))
        left_arg = -abs(monic_poly.degree() * max(monic_poly.coefficients))
        while right_arg - left_arg > eps:
            new_arg = (left_arg + right_arg) / 2
            if monic_poly(new_arg) >= 0:
                right_arg = new_arg
            else:
                left_arg = new_arg
        return left_arg


# Solve Quadratic Equasion
class QuadraticPolynomial(Polynomial):
    def __init__(self, coefficients):
        super().__init__(coefficients)
        # Exception
        if super().degree() > 2:
            raise DegreeIsTooBigException(super().degree())

    def solve(self):
        # Quadratic
        if self.degree() == 2:
            # standard coefficients
            a, b, c = self.coefficients
            # Discriminant
            D = b**2 - 4 * a * c
            # There are no real roots in case of Discriminant < 0
            if D < 0:
                return []
            # Only one root (2 with the same value) in case of Discriminant = 0
            elif D == 0:
                return [-b/(2 * a)]
            # Two different roots in other cases
            else:
                return [(-b - D ** .5)/(2 * a),
                        (-b + D ** .5)/(2 * a)]
        # Linear
        elif self.degree() == 1:
            return [-self.coefficients[1]/self.coefficients[0]]
        # Const
        else:
            # 0 = 0
            if self.coefficients[0] == 0:
                return 'Any x'
            else:
                return []
