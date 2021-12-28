import numpy as np

def first(x, y):
    print(np.ones((x,y)))


def GetMatrix():
    a = [int(x) for x in input().split()]
    b = np.array(a[2:])
    b = np.reshape(b, (a[0], a[1]))
    return b


def second():
    a1 = GetMatrix()
    a2 = GetMatrix()
    try:
        return np.matmul(a1, a2)
    except:
        return "Multiplication is impossible."


def third(x, y, z):
    print(np.linspace(x, y, z))


def forth():
    a1 = GetMatrix()
    a2 = GetMatrix()
    return np.vstack((np.hstack((a1, a2)), np.hstack((a2, a1))))


def fifth(a):
    x = np.zeros((8,8))
    x[1::2,::2] = 1
    x[::2,1::2] = 1
    print(a*x)


def sixth(x, y, z):
    l = np.linspace(x, y-1, y-x)
    a = np.array([x for x in l if x%z == 0], dtype = int)
    return a.reshape((y-x)//z, 1)
