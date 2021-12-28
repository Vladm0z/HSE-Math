def capitalize(string):
    return string.title()

def pangram(string):
    Alph = "abcdefghijklmnopqrstuvwxyz"
    for Symb in Alph:
        if Symb not in string.lower():
            return 'no'
    return 'yes'

def PointInTriangle(x1, y1, x2, y2, x3, y3, x, y):
    a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3)) 
    b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))

    if (0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= (1 - a - b) and (1 - a - b) <= 1) == True:
        return "yes"
    return "no"

def Argsort(seq, direction):
    D = False
    if direction == 'DESC':
        D = True
    Out = [x for x,y in sorted(enumerate(seq), key = lambda x: x[1], reverse=D)]
    print(' '.join(map(str, Out)))
    

def strange_square(x):
    return x**2 - 13

Inp = input()
L = list(map(strange_square, map(int, Inp.split())))
L.sort(key = lambda x: str(abs(x)))
print(' '.join(map(str, L)))

