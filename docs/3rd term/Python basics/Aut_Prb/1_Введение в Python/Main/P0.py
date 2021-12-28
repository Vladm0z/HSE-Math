#Nums = []
#for i in range(2): Nums.append(float(input()))
#print(int(Nums[0]**2 + Nums[1]**2))

#print(int(Nums[0]*Nums[1] % 109))

#Min = int(input())
#print(str(int(Min/60%24)), str(Min%60), sep=":")

#Num = input()
#print(sum(map(int, str(Num))))
#print(int(int(Num)/2)*2 + 2)

#Nums = []
#for i in range(3): Nums.append(float(input()))
#print(int(1+(Nums[0] - Nums[2] - 1)/(Nums[1] - Nums[2])))

#max
Nums = []
for i in range(2): Nums.append(float(input()))
#print(int(((Nums[0] + Nums[1]) + abs(Nums[0] - Nums[1]))/2))

#max2
print(int(Nums[0] -(Nums[0] - Nums[1]) * (((Nums[0] - Nums[1])>>31) & 0x1)))
