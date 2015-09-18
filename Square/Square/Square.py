size = int(raw_input("Enter a number: "))

for i in range(size, 1, -1):
    if i == size:
        print (i*"*")+ (" "*(size-(i+1)))
    else:
        print (i*"*")+ (" "*(size-(i+1)))+("*")

print size*"*"