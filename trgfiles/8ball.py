import random
question = input("Ask the magic 8 ball a question: ")
answer = random.randint(1,8)
goaway = random.randint (1,4)
print ("")
if answer == 1:
    print ("Balls on acurate\n")
elif answer == 2:
    print ("I would probably bet my grannies pension cheque on it\n")
elif answer == 3:
    print ("Bet the farm. Regret is for losers\n")
elif answer == 4:
    print ("Fuck off. I'm napping\n")
elif answer == 5:
    print ("What are you, fucking stupid?  Ask me again.  I dare ya!\n")
elif answer == 6:
    print ("What am I, some kinda fortune teller\n")
elif answer == 7:
    print ("Fuck no\n")
elif answer == 8:
    print ("A fuckton of no.  And another fuckton of no\n") 
else:
    print ("You do know what a question is right?\n")
if goaway == 1:
    print ("Buhbuy. Wait, what? What didn't you understand, the buh or the bye?  Buhbye!\n")
elif goaway == 2:
    print ("Now please find some offs to fuck and fuck off\n")
elif goaway == 3:
    print ("Now make me a happy and leave ok.  OK!\n")
elif goaway == 4:
    print ("10000 idiots all wrapped up in one bundle! Take the hint and leave.\n")
else:
    print ("It's closing time, and even if it's not, it is for me and you.\n")