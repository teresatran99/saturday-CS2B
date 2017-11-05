# Dragon Realm
# A game by Teresa Tran
# 10/7/2017

# import stuff
import random
import time

# global variable
score = 0

# Show Introduction
def show_intro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on site.''')
    print()

def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    return cave


def check_cave(cave_chosen):
    global score
    print("You approach the cave slowly...")
    time.sleep(2)
    print("Smells like dragon farts...")
    time.sleep(2)
    print("A big ol'DRAGON jumps out in front of you and opens its jaws and...")
    print()
    time.sleep(2)

    friendlyDragon = random.randint(1, 2)

    if cave_chosen == str(friendlyDragon):
        print("Gives you his treasure!")
        score += 1
    else:
        print("He farts on you.")
        dodge_fart = random.randint(1, 2)
        print("You try to dodge the fart. Which way? (l or r))")
        dodge = input()
        if dodge == "l" and dodge_fart == "r" :
            print("You dodged the fart!")
        else:
            print("You got hit by the fart!")


    
    print('''Now you must walk across a bridge to reach the second
    checkpoint. You will meet the headmasters of the dragonrealm. One will
    give you a few riddles and the other will test your luck.''')
    time.sleep(3)
    print("You walk across the bridge and realize how unstable it's been constructed-")
    time.sleep(2)
    print('''Run! The board under your feet starts to break and
              it won't be able to hold you up much longer.''')
    time.sleep(2)
    print('''You reach the end of the bridge and see two old men dressed in bizarre
              wizard-like outfits''')
    print("The man on the right introduces himself.")
    time.sleep(2)
    print('''"Hello! I am a headmaster of this realm. If you want to get pass me,
                you have to answer at least one riddle correctly..."''')
    time.sleep(3)
    print("Over fire and over stone,")
    time.sleep(3)
    print("Over water and over bone,")
    time.sleep(3)
    print("Shining out like jewels of light,")
    time.sleep(3)
    print("On a sheet of purest night.")
    time.sleep(3)
    print("What are we?")
    print()

    
    correct_answer = input()
        
    if correct_answer == "stars" and correct_answer == "stars" :
        print("congrats! you shall pass")
    else:
        print("Incorrect! Here's another riddle:")
        time.sleep(3)
        print("I can fly yet have no wings,")
        print("I beat down mountains, I conquer kings,")
        print("At once three different things am I,")
        print("As a continuous whole, I cannot die.")
        print("Do you know who I am?")
        print("HINT: it's not a physical object")
        print()
        correct_answer = input()
    if correct_answer == "time" and correct_answer == "time" :
        print("congrats! you shall pass and receive the treasure,")
        if score <= 1:
            score += 1
        print("Aw, wrong answer. You shall pass without receiving the treasure")
        if score <= 5:
                score -= 5
def play():
    stillPlaying = True
    while stillPlaying:
        show_intro()
        cave = choose_cave()
        check_cave(cave)
        print("Would you like to play again? (y to continue, q to quit)")
        choice = input()
        if choice == "q":
            stillPlaying = False
    print("Your score: " + str(score))
    print("Goodbye! Thanks for playin', naamean?")

# Play the game!
play()




