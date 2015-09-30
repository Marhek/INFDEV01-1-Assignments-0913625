text = raw_input("Write something: ")
new = ""
count = len(text)

while count > 0:
    new += text[count-1]
    count -= 1

print "Reversed:",new