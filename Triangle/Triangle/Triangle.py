size = int(raw_input("Voer een getal in: "))
string = ""

for i in range(0,size+1):
    for j in range(0,i):
        string += "*"
    string += "\n"
print string