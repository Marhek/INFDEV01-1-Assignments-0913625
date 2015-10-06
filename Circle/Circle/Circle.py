from math import *

size = int(raw_input("Voer een getal in: "))
string = ""

for i in range(0,size*2):
    for j in range(0,size*2):
        di = (i - size)**2
        dj = (j - size)**2
        dist = sqrt(di + dj)

        if size > dist:
            string += "*"
        else:
            string += " "

    string += "\n"
print string