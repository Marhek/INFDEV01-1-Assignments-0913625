size = int(raw_input("Voer een getal in: "))

for i in range(size,1,-1):
    if i == size:
        print size*"*"
    else:
        print "*"+(i-1)*"*"+(size-(i+1))*" "+"*"

print size*"*"