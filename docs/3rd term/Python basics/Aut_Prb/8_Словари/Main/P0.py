def Sells():
    with open("input.txt", "r") as file, open("output.txt", "w") as Outp: 
        D = {}
        for line in file:
            Cont = line.split()
            if (str(Cont[0]) + ' ' + str(Cont[1])) in D.keys():
                D[str(Cont[0]) + ' ' + str(Cont[1])] = D[str(Cont[0]) + ' ' + str(Cont[1])] + int(Cont[2])
            else:
                D[str(Cont[0]) + ' ' + str(Cont[1])] = int(Cont[2])
        K_0 = ''
        for k in sorted(D):
            K = k.split()
            if K_0 != K[0]:
                K_0 = K[0]
                Outp.write(str(K_0) + ': \n')
            Outp.write(str(K[1]) + ' ' + str(D[k]) + ' \n')


def Access():
    D = {}
    Outp = ''
    for i in range(int(input())):
        Cont = input().split()
        D[str(Cont[0])] = str(Cont[1:])
    for i in range(int(input())):
        Cont = input().split()
        if Cont[0] == 'read' and 'R' in D[Cont[1]]:
            Outp = Outp + 'OK'
        elif Cont[0] == 'write' and 'W' in D[Cont[1]]:
            Outp = Outp + 'OK'
        elif Cont[0] == 'execute' and 'X' in D[Cont[1]]:
            Outp = Outp + 'OK'
        else:
            Outp = Outp + 'Access denied'
        Outp = Outp + '\n'
    print(Outp)

import string

def char_freq(str1):
    dict = {}
    for n in string.ascii_lowercase:
        dict[n] = 0
    for n in str1:
        dict[n] += 1
    return dict

def Anagram_1():
    Line_0 = input()
    Line_1 = input()
    D_0 = char_freq(Line_0[0:len(Line_1)])
    D_1 = char_freq(Line_1)
    if D_0 == D_1:
        return 'YES'
    for i in range(0, len(Line_0)-len(Line_1)):
        D_0[Line_0[i]] -= 1
        D_0[Line_0[i+len(Line_1)]] += 1
        print(D_0)
        if D_0 == D_1:
            return 'YES'
    return 'NO'

print(Anagram_1())
    
