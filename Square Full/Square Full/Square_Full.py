size = int(raw_input("Enter a number: " ))
string = ""

for i in range(size,0,-1):
    for j in range(size,0,-1):
        string += "*"
    string += "\n"
print string