text = raw_input("Password: ")
points = 0
numbers = 0
count = len(text)
lower = False
upper = False
special = 0

if count >= 15:
    points += 3
elif count >= 10:
    points += 2
elif count >= 5:
    points += 1

while count > 0:
    if text[count-1].isdigit():
        numbers += 1
    elif text[count-1].islower():
        lower = True
    elif text[count-1].isupper():
        upper = True
    else:
        special += 1
    count -= 1

if numbers >= 5:
    points += 3
elif numbers > 2:
    points += 2
elif numbers >= 1:
    points += 1

if lower and upper:
    points += 1

if special > 0:
    points += special

if points > 6:
    print text,"is a STRONG password"
elif points > 3:
    print text,"is a MEDIUM password"
else:
    print text,"is a WEAK password"