size = int(raw_input("Enter a number: "))

for i in range(size,0,-1):
    if i == 1 or i == size:
        print size*"*"
    else:
        print "*"+" "*(size-2)+"*"