#Nums = []
#for i in range(2): Nums.append(int(input()))
#for num in range(Nums[0], Nums[1]+1):
#    print(num)
#for num in range(int((Nums[0]+1)/2), int(Nums[1]/2)+1):
#    print(2*num)

#Inp = []
#n = input()
#while n != 'END':
#    Inp.append(n)
#    n = input()
#for num in Inp:
#    print(num)

#Sum = 0
#n = input()
#while n != '-1000':
#    Sum += int(n)
#    n = input()
#print(Sum)

#pos = 0
#n = int(input())
#for i in range(n):
#    if int(input())>0: pos += 1
#print(pos)

#Nums = []
#for i in range(2): Nums.append(int(input()))
#Min = min(Nums[0], Nums[1])
#if Nums[0] < Nums[1]:
#    for i in range(abs(Nums[0]-Nums[1])+1):
#        print(Min + i)
#else:
#    for i in range(abs(Nums[0]-Nums[1])+1):
#        print(Min + abs(Nums[0]-Nums[1]) - i)

#n = int(input())
#outp = 1
#for i in range(1,n+1):
#    outp = outp * i
#print(outp)

#w = input()
#space = 0
#for i in str(w):
#    if i == ' ':
#        space += 1
#print(space)


n = int(input())
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
for i in m:
#    print(*i, sep = ' ')
    i = [str(j).rjust(len(str(m[-1][-1]))+1) for j in i]
    print(''.join(i))
