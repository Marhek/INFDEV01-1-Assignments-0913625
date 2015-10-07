size = int(raw_input("Voer een onevengetal in: "))
string = ""

for i in range(1,size+1,2):
    for s in range(size/2,-1,-1):
        string += " "
    for j in range(i):
        string += "*"
    string += "\n"
print string