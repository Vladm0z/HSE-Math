def Dict():
    n = int(input())
    D = {}
    for i in range(0,n):
        a = list(input().split(' '))
        D[a[0]] = a[1]
    print(D)


def Synonym():
    n = int(input())
    D_1 = {}
    D_2 = {}
    for i in range(0,n):
        a = list(input().split(' '))
        D_1[a[0]] = a[1]
        D_2[a[1]] = a[0]
    w = input()
    if w in D_1.keys():
        return D_1[w]
    return D_2[w]

def Sq(n):
    D = {}
    for i in range(1, n+1):
        D[i] = i**2
    return D


def SumD():
    D_1 = {i.split(':')[0]: i.split(':')[1] for i in input().split(' ')}
    D_2 = {i.split(':')[0]: i.split(':')[1] for i in input().split(' ')}
    D_2.update(D_1)
    return D_2


def StrN_1():
    D = {i: j for i, j in enumerate(input().split(' '))}
    D = {k: v for k, v in sorted(D.items(), key=lambda item: int(item[1]))}
    Out = '['
    for k, v in D.items():
        Out += f'({k}, {v}), '
    print(Out[:len(Out)-2] + ']')

def StrN_2():
    Inp = list(map(int, input().split())) 
    Z = list(zip(range(len(Inp)), Inp))
    D = dict(Z)
    D1 = sorted(D.items(), key=lambda x: x[1])  
    print(D1)

def CommonWord():
    D = {}
    D_1 = {}
    Inp = list(input().split())
    for i in Inp:
        if i not in D.keys():
            D[i] = 1
        else:
            D[i] += 1
    D = {k: v for k, v in sorted(D.items(), key=lambda x: x[1], reverse=True)}
    for i in D.keys():
       if D[i] == max(D.values()):
           D_1[i] = D[i]
    D_1 = sorted(list(D_1.keys()))
    print(D_1[0])

CommonWord()

