Numbers = [] 
Total = 0 
with open("input.txt", "r+") as Inp, open("output.txt", "w") as Outp: 
    InpLines = Inp.readlines()
    for line in InpLines: Numbers += line.strip().split(" ")
    for number in Numbers: Total += int(number)
    Outp.write(str(Total))
