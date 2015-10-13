size = int(raw_input("Voer een onevengetal in: "))
string = ""
height = (size+1)/2

for i in range(1,height+1):
    for s in range(height-i):
        string += " "
    for j in range((i*2)-1):
        string += "*"
    string += "\n"
print string