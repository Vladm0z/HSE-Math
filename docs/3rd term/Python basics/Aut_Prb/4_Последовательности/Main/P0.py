#a, b = map(int, input().split())
#N = ['I']*a
#for i in range(b):
#    x, y = map(int, input().split())
#    for j in range(x-1, y):
#        N[j] = '.'
#Ns = ''.join(str(k) for k in N)
#print(Ns)

#Inp = list(map(int, input().split()))
#Out = [max(Inp) if x == min(Inp) else min(Inp) if x == max(Inp) else x for x in Inp]
#OutS = ' '.join(str(i) for i in Out)
#print(OutS)

#a, b = map(int, input().split())
#M = []
#for i in range(a): 
#    M.append([int(j) for j in input().split()])
#MaE = 0
#MaC = None
#for i, row in enumerate(M):
#    for j, col in enumerate(row):
#        if col > MaE:
#            MaE = col
#            MaC = (i, j)
#MaCS = ' '.join(str(i) for i in MaC)
#print(MaCS)

#print(sum(map(sum, [list(map(int, input().split())) for _ in range(int(input()))])))

#for k in [list(map(lambda x: x*3, input().split())) for _ in range(int(input()))]: print(' '.join(k))

#M1 = [list(map(int, input().split())) for _ in range(int(input()))]
#M2 = [list(map(int, input().split())) for _ in range(int(input()))]
#for k in [[sum(m1*m2 for m1, m2 in zip(M1_row,M2_col)) for M2_col in zip(*M2)] for M1_row in M1]: print(' '.join(str(l) for l in k))

#M = [list(map(int, input().split())) for _ in range(int(input()))]
#for k in [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]: print(' '.join(str(l) for l in k))
