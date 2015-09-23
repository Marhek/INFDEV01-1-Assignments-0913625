print "We are going to play Rock, Paper, Scissors, Lizard, Spock."
print "r = Rock, p = Paper, s = Scissors, l = Lizzard, v = Spock"
print "First write down your choices and then fill them in here."

p1 = raw_input("Player 1 choice: ")
a1 = False
p2 = raw_input("Player 2 choice: ")
a2 = False

if p1 == "r" or p1 == "p" or p1 == "s" or p1 == "l" or p1 == "v":
    a1 = True
if p2 == "r" or p2 == "p" or p2 == "s" or p2 == "l" or p2 == "v":
    a2 = True

while a1 == False or a2 == False:
    if a1 == False:
        print "Player 1 this is an invalid choice"
        p1 = raw_input("Player 1 choose again: ")

        if p1 == "r" or p1 == "p" or p1 == "s" or p1 == "l" or p1 == "v":
            a1 = True
    if a2 == False:
        print "Player 2 this is an invalid choice"
        p2 = raw_input("Player 2 choose again: ")

        if p2 == "r" or p2 == "p" or p2 == "s" or p2 == "l" or p2 == "v":
            a2 = True

#Player 1 wins
#Rock vs ...
if p1 == "r" and p2 == "s":
    print "Rock crushes Scissors"
    print "Player 1 WINS!"
elif p1 == "r" and p2 == "l":
    print "Rock crushes Lizard"
    print "Player 1 WINS!"
#Lizard vs ...
elif p1 == "l" and p2 == "p":
    print "Lizard eats Paper"
    print "Player 1 WINS!"
elif p1 == "l" and p2 == "v":
    print "Lizard poisons Spock"
    print "Player 1 WINS!"
#Spock vs ...
elif p1 == "v" and p2 == "s":
    print "Spock smashes Scissors"
    print "Player 1 WINS!"
elif p1 == "v" and p2 == "r":
    print "Spock vaporizes Rock"
    print "Player 1 WINS!"
#Scissors vs ...
elif p1 == "s" and p2 == "p":
    print "Scissors cuts Paper"
    print "Player 1 WINS!"
elif p1 == "s" and p2 == "l":
    print "Scissors decapitates Lizard"
    print "Player 1 WINS!"
#Paper vs ...
elif p1 == "p" and p2 == "r":
    print "Paper covers Rock"
    print "Player 1 WINS!"
elif p1 == "p" and p2 == "v":
    print "Paper disproves Spock"
    print "Player 1 WINS!"
#Player 2 wins
#Rock vs ...
elif p2 == "r" and p1 == "s":
    print "Rock crushes Scissors"
    print "Player 2 WINS!"
elif p2 == "r" and p1 == "l":
    print "Rock crushes Lizard"
    print "Player 2 WINS!"
#Lizard vs ...
elif p2 == "l" and p1 == "p":
    print "Lizard eats Paper"
    print "Player 2 WINS!"
elif p2 == "l" and p1 == "v":
    print "Lizard poisons Spock"
    print "Player 2 WINS!"
#Spock vs ...
elif p2 == "v" and p1 == "s":
    print "Spock smashes Scissors"
    print "Player 2 WINS!"
elif p2 == "v" and p1 == "r":
    print "Spock vaporizes Rock"
    print "Player 2 WINS!"
#Scissors vs ...
elif p2 == "s" and p1 == "p":
    print "Scissors cuts Paper"
    print "Player 2 WINS!"
elif p2 == "s" and p1 == "l":
    print "Scissors decapitates Lizard"
    print "Player 2 WINS!"
#Paper vs ...
elif p2 == "p" and p1 == "r":
    print "Paper covers Rock"
    print "Player 2 WINS!"
elif p2 == "p" and p1 == "v":
    print "Paper disproves Spock"
    print "Player 2 WINS!"
#Draw
else:
    print "It's a draw, nobody wins"