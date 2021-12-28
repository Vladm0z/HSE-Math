def CapH(S):
    try:
        a1 = S.index('h')
        a2 = S.rindex('h')
    except ValueError:
        a1 = a2 = 0
    if a1 == a2:
        if a1 == 0:
            return S
        return S[:a1] + S[a1].lower() + S[a1+1:]
    return S[:a1] + S[a1].lower() + S[a1+1:a2].replace('h', 'H') + S[a2].lower() + S[a2+1:]

def Symb124(S):
    S = list(S)
    del S[0::3]
    return ''.join(S)


def Palindrome(S):
    S = S.translate(str.maketrans('', '', '\'"!#$%&()*+,-./:;<=>?@[]^_`{|}~ 0123456789')).lower()
    for i in range(0, int(len(S)/2)):
        if S[i] != S[len(S)-i-1]:
            return 'NO'
    return 'YES'

def BANANA(S):
    V = 0
    S = list(S)
    for i in range(0,len(S)):
        if S[i] in 'AEIOU':
            V = V + len(S) - i
    P = int((len(S)*(len(S) + 1)/2) - V)
    print(P)
    print(V)
    if P > V:
        return 'Petya ' + str(P)
    elif P < V:
        return 'Vasya ' + str(V)
    return 'Draw'

def TripleQ(S):
    S = S.translate(str.maketrans('', '', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>@[]^_`{|}~'))
    S = S.replace('???', '')
    M = 0
    N = 0
    for i in range(0, len(S)-1):
        if S[i] in '0123456789' and S[i+1] in '0123456789':
            if int(S[i]) + int(S[i+1]) == 10:
                M += 1
    S = list(S.translate(str.maketrans('', '', '?')))
    for i in range(0, len(S)-1):
        if S[i] in '0123456789' and S[i+1] in '0123456789':
            if int(S[i]) + int(S[i+1]) == 10:
                N += 1
    if N == M != 0:
        return 'YES'
    return 'NO'


def ColRowSum():
    with open("input.txt", "r") as file, open("output.txt", "w") as Outp: 
        R = []
        C = []
        for line in file:
            L = list(map(lambda x: float(x.replace(',','.')), line.split()))
            if R == []: R = [0]*len(L)
            for i in range(0, len(L)):
                R[i] = R[i] + L[i] 
            C.append(sum(L))
        R = list(map(lambda x: str('{:.1f}'.format(round(x,1))).replace('.',','), R))
        C = list(map(lambda x: str('{:.1f}'.format(round(x,1))).replace('.',','), C))
        #m = len(max((sub[0] for sub in [C, R]),key=len))
        m = len('100.0')
        Out = ' '.join(['{:>{m}}'.format(n,m=m) for n in C]) + '\n' + ' '.join(['{:>{m}}'.format(n,m=m) for n in R])
        Outp.write(Out)


def PyFun(S):
    s, n = S.split()
    n = int(n)
    if n < 1:
        print()
    elif n == 1:
        print(' '.join(s))
    elif n > len(s):
        print('\n'.join(s))
    else:  
        Out = [[' ']*len(s) for i in range(n)]
        for i in range(0, len(s)):
            if i%(2*n - 2) == 0:
                r = 0
                c = i//(2*n - 2)*(n-1)
            elif i%(2*n - 2) < n:
                r += 1
            else:
                r -= 1
                c += 1
            Out[r][c] = s[i]
        if n == 2:
            for line in Out:
                print('  '.join(line))
        else:
            for line in Out:
                a = list(' '.join(line))
                for i in range(0, int((len(a)-1)/2)):
                    if i%(n-1) != 0 and i%(n-1) != n-2:
                        a[2*i+1] = ''
                print(''.join(a))

                