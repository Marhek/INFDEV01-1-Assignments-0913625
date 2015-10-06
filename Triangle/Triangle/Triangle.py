size = int(raw_input("Voer een getal in: "))
string = ""

for i in range(0,size):
    string += (i+1)*"*"+"\n"

print string