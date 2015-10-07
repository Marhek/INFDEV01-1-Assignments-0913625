from math import *

size = int(raw_input("Voer een getal in: "))
string = ""

for i in range(0,size*2):
    for j in range(0,size*2):
        di = (i - size)**2
        dj = (j - size)**2
        dist = sqrt(di + dj)

        if size > dist and size-2 < dist:
            string += "*"
        elif (i == size/2 and j == size/2) or (i == size/2 and j == size+size/2):
            string += "0"
        elif (i == (size/2)-1 and j == size/2) or (i == (size/2)-1 and j == size+size/2):
            string += "_"
        elif i == size and j == size:
            string += "L"
        elif i == size+size/2 and (j > size/2 and j < size+size/2):
            string += "-"
        elif i == size+(size/2)-1 and (j == (size/2)-1 or j == (size+size/2)+1):
            string += "_"
        else:
            string += " "

    string += "\n"
print string