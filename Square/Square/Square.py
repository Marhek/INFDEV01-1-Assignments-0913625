size = int(raw_input("Enter a number: " ))
string = ""

for i in range(size,0,-1):
    for j in range(size,0,-1):
        if i == 1 or i == size:
            string += "*"
        elif j == 1 or j == size:
            string += "*"
        else:
            string += " "
    string += "\n"
print string