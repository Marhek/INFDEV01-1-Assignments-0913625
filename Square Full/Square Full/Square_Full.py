size = int(raw_input("Enter a number: " ))
string = ""

for i in range(size,0,-1):
    string += size*"*"+"\n"

print string