def cube(a):
    return a**3

def cost(item='апельсин', amount=10, price=150):
    print(f'{amount} kilos of {item}, which price is {price}, cost {amount * price}')

def P(x):
    return 5*x**3 - 10*x**2 + 47*x + 9

#spisok = list(map(int, input().split()))
#spisok_1 = list(map(lambda x: x**2, map(int, input().split())))
#spisok_2 = sorted(list(input().split()), key=lambda x: x[1])
#spisok_3 = sorted(list(map(int, input().split())), key=lambda x: abs(x))
#print(' '.join(str(x) for x in spisok_3))

a = input()
for i, t in enumerate(zip(a)): print(i, t[0])
