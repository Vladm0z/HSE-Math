#def Triplets(a,b,c):
#        if ((a+b-c)<0 or (a-b+c)<0 or (-a+b+c)<0): print('impossible')
#        elif ((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)): print('right')
#        elif ((a**2 + b**2 > c**2) and (a**2 + c**2 > b**2) and (b**2 + c**2 > a**2)): print('acute')
#        else: print('obtuse')

#Nums = []
#for i in range(4): Nums.append(float(input()))
#Triplets(Nums[0], Nums[1], Nums[2])
#print(((Nums[0]+Nums[1])%2 == (Nums[2]+Nums[3])%2)*'YES' + ((Nums[0]+Nums[1])%2 != (Nums[2]+Nums[3])%2)*'NO')


#def Chess(piece, x1, y1, x2, y2):
#        if (piece == 'bishop' and abs(x1-x2) == abs(y1-y2)): print('YES')
#        elif (piece == 'king' and abs(x1-x2) <= 1 and abs(y1-y2) <= 1): print('YES')
#        elif (piece == 'rook' and (x1-x2)*(y1-y2) == 0): print('YES')
#        elif (piece == 'queen' and ((abs(x1-x2) == abs(y1-y2)) or ((x1-x2)*(y1-y2) == 0))): print('YES')
#        elif (piece == 'knight' and ((abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2))): print('YES')
#        else: print('NO')

#Chs = []
#for i in range(5): Chs.append(input())
#Chess(Chs[0], int(Chs[1]), int(Chs[2]), int(Chs[3]), int(Chs[4]))        


#def Chocolate(n,m,k):
#        if (k>=n*m): print('NO')
#        elif ((k%n==0) or (k%m==0)): print('YES')
#        else: print('NO')

#Choco = []
#for i in range(3): Choco.append(int(input()))
#Chocolate(Choco[0], Choco[1], Choco[2])
