print "We are going to play Rock, Paper, Scissors."
print "r = Rock, p = Paper, s = Scissors"
print "First write down your choices and then fill them in here."

p1 = raw_input("Player 1 choice: ")
a1 = False
p2 = raw_input("Player 2 choice: ")
a2 = False

if p1 == "r" or p1 == "p" or p1 == "s":
    a1 = True
if p2 == "r" or p2 == "p" or p2 == "s":
    a2 = True

while a1 == False or a2 == False:
    if a1 == False:
        print "Player 1 this is an invalid choice"
        p1 = raw_input("Player 1 choose again: ")

        if p1 == "r" or p1 == "p" or p1 == "s":
            a1 = True
    if a2 == False:
        print "Player 2 this is an invalid choice"
        p2 = raw_input("Player 2 choose again: ")

        if p2 == "r" or p2 == "p" or p2 == "s":
            a2 = True

if p1 == "r" and p2 == "s":
    print "Rock beats Scissors"
    print "Player 1 WINS!"
elif p1 == "s" and p2 == "p":
    print "Scissors beats Paper"
    print "Player 1 WINS!"
elif p1 == "p" and p2 == "r":
    print "Paper beats Rock"
    print "Player 1 WINS!"
elif p2 == "r" and p1 == "s":
    print "Rock beats Scissors"
    print "Player 2 WINS!"
elif p2 == "s" and p1 == "p":
    print "Scissors beats Paper"
    print "Player 2 WINS!"
elif p2 == "p" and p1 == "r":
    print "Paper beats Rock"
    print "Player 2 WINS!"
else:
    print "It's a draw, nobody wins"