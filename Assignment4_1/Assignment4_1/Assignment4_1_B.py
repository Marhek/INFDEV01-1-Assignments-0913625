c = float(raw_input("Hoeveel graden Celcius: "))

while c < -273.15:
    print "This number is under the absolute 0. Try again."
    c = float(raw_input("Hoeveel graden Celcius: "))

k = round(c+273.15,2)
print "Graden Kelvin:",k