def DelSymb(x):
    return print(''.join(dict.fromkeys(x)))


def Sequences():
    n = set(list(range(1, int(input())+1)))
    seq_1 = set(map(int, input().split(' ')))
    seq_2 = set(map(int, input().split(' ')))
    print(' '.join(str(x) for x in sorted(list(set.intersection(seq_1, seq_2)))))
    print(' '.join(str(x) for x in sorted(list(n - seq_1 - seq_2))))


def NumGuess():
    n, m = map(int, input().split(' '))
    rg = set(list(range(-n, n)))
    for i in range(m):
        ans = input()
        if 'YES' in ans:
            rg = set.intersection(rg, set(map(int, ans[:len(ans) - 4].split(' '))))
        else:
            rg = rg - set(map(int, ans[:len(ans) - 3].split(' ')))
    if len(rg) == 1:
        print('YES')
    else:
        print('NO')
        
def Scheme():
    I = sorted(list(set(map(int, input().split(' ')))))
    O = [I[0]]
    i = 0
    a = 0
    while i < len(I):
        if i == len(I)-1:
            O.append(a)
            break
        if I[i] + 1 == I[i+1]:
            a += 1
        else:
            O.append(a)
            O.append(I[i+1])
            a = 0
        i += 1
    Out = ''
    for i in range(len(O)//2):
        if O[2*i+1] != 0:
            Out += str(O[2*i]) + '-' + str(O[2*i]+O[2*i+1]) + ','
        else:
            Out += str(O[2*i]) + ','
    print(Out[:len(Out)-1])


def Common(x):
    L = list(map(int, x.split(' ')))
    n = len(L)
    freq = {}
    for i in range(n):
        if L[i] in freq:
            freq[L[i]] += 1
        else:
            freq[L[i]] = 1
    max_freq = 0
    for i, j in freq.items():
        max_freq = max(max_freq, j)
    return n - max_freq


def SubSeq(a, n, s=0, beg=0):
    for i in range(len(a)):
        if s < n:
            s += a[i]
            while s > n:
                s -= a[beg]
                beg += 1
            if s == n:
                return print(beg, i)
        elif s == n:
            return print(beg, i)
        else:
            s -= a[beg]
            beg += 1
    return print('None')


SubSeq(list(map(int, input().split())), int(input()))


        
        
