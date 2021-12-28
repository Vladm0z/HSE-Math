
def Set_1(x):
    x = sorted(list(set(x.split(' '))), key = lambda i: int(i))
    print(' '.join(x))

def Set_2():
    x = []
    a = int(input())
    while a != 0:
        x.append(a)
        a = int(input())
    x = sorted(set(x), key = lambda i: int(i))
    print(' '.join(map(str, x)))
    

print(' '.join(sorted(list(set(input().split(' ')) | set(input().split(' '))), key = lambda i: str(i))).strip())

#print(len(set(input().split(' '))))
    
#print(len(set(list(set(input().split(' ')) & set(input().split(' '))))))

#print(len(set(input().replace('  ', ' ').split(' '))))

def Sets():
    a = int(input())
    x = []
    z = set()
    for i in range(a):
        x.append(set(input().split(' ')))
    y = x[0]
    for j in range(a):
        y = sorted(list(set(y) & x[j]), key = lambda i: int(i))
    for j in range(a):
        z = sorted(list(set(z) | x[j]), key = lambda i: int(i))
    print(' '.join(y))
    print(' '.join(z))

