text = raw_input("text: ")
number = int(raw_input("number: "))

count = 0
newtext = ""

while count < len(text):
    i = text[count]

    if i.islower():
        i = ord(i)+number
        while i > 122:
            i = 96 + (i - 122)
        while i < 97:
            i = 123 - (97 - i)
        newtext += chr(i)
    elif i.isupper():
        i = ord(i)+number
        while i > 90:
            i = 64 + (i - 90)
        while i < 65:
            i = 91 - (65 - i)
        newtext += chr(i)
    else:
        newtext += i

    count += 1
print "Result:",newtext