size = int(raw_input("Enter a number: "))

for i in range(size, 0, -1):
    if i == size or i == 0:
        print size*"*"
    else:
        print "*"+(i-2)*" "+"*"