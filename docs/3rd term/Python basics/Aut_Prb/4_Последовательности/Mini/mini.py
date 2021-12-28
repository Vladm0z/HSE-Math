#n = int(input())
#Words = []
#for i in range(n): Words.append(input())
#for i in range(n): Words.append(int(input()))
#print(Words)
#print(*Words, sep='!')

#Words = input().split(', ')
#print(Words)

#Nums = [int(i) for i in input().split(' ')]
#print(len(Nums), Nums.count(0), sep='\n')
#if Nums.count(4) > 0: print('True')
#else: print('False')
#print(sum(Nums), Nums*2, sep='\n')
#if max(Nums) == min(Nums): print(min(Nums))
#else: print(max(Nums), min(Nums), sep=' ')

#Nums = []
#a, b = input().split(' ')
#for i in range(int(a)):
#    Nums.append([int(i) for i in input().split(' ')])
#    Nums.append([int(i)+1 for i in input().split(' ')])
#print(Nums)
#for i in Nums:
#    print(*i)

#HTP3SB
W = input()
print(len(W))
for i in range(0, len(W), 2):
    print(W[i], end='')
print()
for i in range(1, len(W), 2):
    print(W[i], end='')
print()
print(W[0], W[-1], sep=' ')
print(W[:-5-1:-1])
