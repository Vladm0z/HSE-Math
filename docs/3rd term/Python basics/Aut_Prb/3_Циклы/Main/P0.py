#i = int(input())
#n = 2
#c = 1
#while n*2 <= i:
#    n = n*2
#    c += 1
#print(str(n), str(c))


#n = int(input())
#Nums = []
#for i in range(n): Nums.append(int(input()))
#max_value = max(Nums)
#max_index = Nums.index(max_value)
#print(max_value, max_index)

#n = int(input())
#s = 0
#for i in range(1, n+1):
#    a = 1
#    for j in range(1, i+1):
#        a = a * j
#    s += a
#print(s)

#a = int(input())
#b = int(input())
#c = a*b
#while b > 0:
#    a, b=b, a%b
#c = c/a
#print(int(a), int(c))

#тут я был не трезв
#a = -9999
#b = -9999
#while True:
#    i = int(input())
#    if i == 0: break
#    if i > a:
#        b = a
#        a = i
#    if a > i > b:
#        b = i
#print(b)

#m = 0
#c = 0
#while True:
#    i = int(input())
#    if i == 0: break
#    if i == m:
#        c += 1
#    if i > m:
#        m = i
#        c = 1
#        print(i)
#print(c)

#n = 1
#n1 = 0
#n2 = 1
#c = 1
#i = int(input())
#while n < i:
#    n = n1 + n2
#    n1 = n2
#    n2 = n
#    c += 1
#if n == i: print(c)
#else: print(-1)
