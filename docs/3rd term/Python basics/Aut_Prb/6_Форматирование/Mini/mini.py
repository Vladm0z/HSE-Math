import string

def IsPunct(x):
    if x in string.punctuation:
        return True
    return False


#print(a.find('abc'))
#print(a.replace(',', '.'))
#print(a.count(' '))
#print(str(sum(char.isalpha() for char in a)), str(sum(char.isdigit() for char in a)), sep=' ')

#a = int(input())
#Files = []
#for file in range(a): Files.append(input())
#for file in Files:
#    if file.startswith('Python_for_study/') and (file.endswith('.py') or file.endswith('.ipynb')):
#        print(file)

#a, b = input().strip('_').split()
#print(a.upper(), b.lower(), sep=' ')

#for i in input(): print(chr(ord(i)-3), end='')

#name, sex, weight, age, mark = input().split()
#txt = 'Mark: {mark}, name: {name}, age: {age}, weight: {weight}, sex: {sex}.'
#print(txt.format(mark = mark, name = name, age = 2021 - int(age), weight = weight, sex = sex))

#m1, m2 = map(lambda x: '{:.3f}'.format(round(x, 3)) ,map(float, input().split()))
#txt = 'My metrcis'+ '\n' + '-'*10 + '\n' + 'metrics_1' + '\t' + '{metrics_1}' + '%' + '\n' + 'metrics_2' + '\t' + '{metrics_2}' + '%' + '\n' + '-'*10
#print(txt.format(metrics_1 = m1, metrics_2 = m2))


with open("input.txt", "r") as Inp, open("output.txt", "w") as Outp: 
    N = 0
    InpLines = Inp.readlines()
    for line in InpLines: N += 1
    Outp.write(str(N))
