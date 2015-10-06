size = int(raw_input("Voer een getal in: "))
string = ""

for i in range(1,size+1,+2):
    string += (size-i)/2*" "+i*"*"+"\n"

print string