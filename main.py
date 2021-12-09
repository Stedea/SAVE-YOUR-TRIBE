from random import randint
from time import sleep

# A COUPLE OF NOTES:
# We do not use print() for story-telling, we use printWait() since it automatically sleeps
# We do not use input() for inputs, we use getInput(["optionA","optionB"...])
# For yes or no questions, use askYesOrNo() which either returns True or False

lives = 3
treasure = 0
currentQuiz = 1

positiveAnswers = [
    "y", "yes", "yeah", "aha", "affirmative", "true", "t", "sure", "yup",
    "yarp", "yeth", "yarrr, it's rewind time", "oui"
]
negativeAnswers = [
    "n", "no", "nope", "negative", "false", "f", "nah", "narp", "non", "nyet",
    "how dare you", "u stoopid"
]

quizList = [
    # ["question", "answer", True]
    ["10 + 9", "19", True],
    ["16 * 2", "49", False],
    ["5 * 3 - 1", "15", False],
    ["9 + 10", "21", False],
    ["10 + 2", "12", True],
    ["100 + 100", "100 * 2", True],
    ["10 - 4", "4", False],
]


# function to wait an appropriate amount of time before sending next message
# the longer the message the longer it waits
# implemented by: Vlad
# "sleep" must be imported from the "time" module. *Ohh yeah it's sleep time*
def printWait(text):
    words = len(text.strip().split(" "))
    print(text)
    # average readin speed is 4.2wps so we divide words by time it takes to read them
    # randint used here to make waiting time more random to seem less repetitive
    sleep(words / (randint(400, 440) / 100))


def validateIntegerInput(num):
    # for this do variable = validateIntegerInput(otherVariable)
    while not num.isnumeric():
        num = input("Please enter an actual number: ")
    return (num)


def askYesOrNo():
    choice = input("Please enter your choice [\"y\", \"n\"]: ")
    while choice.lower() not in positiveAnswers and choice.lower() not in negativeAnswers:
        choice = input("Please enter a valid option [\"y\", \"n\"]: ")

    if choice in positiveAnswers:
        return (True)
    else:
        return (False)


def getInput(options):
    # options must be an array of LOWERCASE options so ["a","b","c"]
    firstLetterOptions = []
    for i in options:
        firstLetterOptions.append(i[0])

    answer = input("Please enter your choice " + str(options) + ": ")
    while answer.lower() not in options and answer.lower() not in firstLetterOptions:
        answer = input("Please enter a valid option " + str(options) + ": ")
    return (answer)


# function to save scores
def saveScores():
    # open in append mode
    scoresFile = open("scores.csv", "a")
    scoresFile.write("\n" + myName + ", " + str(treasure) + ", " + str(lives))
    scoresFile.close()


def quiz(questionNumber):
    global lives
    print("===")
    print("Question " + str(questionNumber) + ":")
    i = randint(0, len(quizList) - 1)

    while lives > 0:
        answer = input("Is " + quizList[i][0] + " equal to " + quizList[i][1] +": ")
        if (answer.lower() in positiveAnswers and quizList[i][2]) \
          or (answer.lower() in negativeAnswers and not quizList[i][2]):
            printWait("Well done Hero!!!")
            break
        else:
            printWait("Try again")
            lives = lives - 1
            printWait("You have lost 1 life, you have " + str(lives) +" lives left")
    quizList.remove(quizList[i])


# Ogre guessing game
def ogreGame():
    global myName

    guessesTaken = 0
    printWait('Hello! What is your name?')
    myName = input()
    number = randint(1, 20)
    printWait('Well, ' + myName +', I am thinking of a number between 1 and 20.')
    while guessesTaken < 6:
        printWait('Take a guess.')
        guess = input()
        if not guess.isnumeric():
            printWait("Please enter an integer")
            guessesTaken = guessesTaken + 1
            continue

        guess = int(guess)

        guessesTaken = guessesTaken + 1
        if guess < number:
            printWait('Your guess is too low.')
        elif guess > number:
            printWait("Your guess is too high")
        elif guess == number:
            printWait('Good job, ' + myName + '! You guessed my number in ' +str(guessesTaken) + ' guesses!')
            # Code after guessing game
            printWait("Well done you escaped the ogre")
            printWait("However the ogre does not like the fact that you beat him")

            printWait("So as you were leaving he closed the door on you and then ate you")
            printWait("You died")
            input("Press any key to exit: ")
            exit()
    printWait("WRONG!!!")
    printWait('Nope. The number I was thinking of was ' + number)
    printWait("The ogre kills you")
    input("Press any key to exit: ")
    exit()


# Initial game code
print("""    ████████████████████████████████████    
  ██                                    ██  
██                                        ██
██                                        ██
██        ████    ██    ██  ██████        ██
██      ██    ██  ██  ██          ██      ██
██      ██    ██  ████        ████        ██
██      ██    ██  ██  ██                  ██
██        ████    ██    ██    ██          ██
██                                        ██
██                                        ██
  ██                                    ██  
    ██████      ████████████████████████    
        ██      ██              
        ██      ██  THE DUNGEON GAME 
      ██      ██     - by Stephen
      ██    ██       - by Vlad
      ██████         - by Mateusz
      ██             
    """)
printWait("You are in a town that is going to be destroyed in a few weeks by the Gazula tribe")
printWait("You are the brave warrior that has been chosen to save the town")
printWait("You must now enter a 'do or die quest' to save your town")
printWait("However, you only have 3 lives to complete this quest so if you die after 3 times you will stay dead")
printWait("Have fun!")
print("---")
printWait("Here is your first challenge brave warrior")
printWait("Your first challenge is an easy one. All you have to do is get 3 simple questions right.")
printWait("You can answer the true or false questions with the first letter of the word")

# True or false game (3 questions)
for i in range(currentQuiz, 4, 1):
    quiz(i)
    currentQuiz = currentQuiz + 1

if lives == 0:
    print("You ran out of lives. A Gazualian gnome shoots you with a poison dart.")
    input("Press any key to exit: ")
    exit()

print("---")

# Directions to different paths
# True or false quiz complete
# Experimentation with multi-line strings
printWait("Well done, you have completed your first challenge")
printWait("You now have to choose a pathway to travel down")

answer = getInput(["left", "right", "down"])
if answer.lower() == "left" or answer.lower() == "l":
    treasure = treasure + 150
    printWait("You have found a very small treasure room, you now have " +str(treasure) + " treasure")
    printWait("If you chose the left (which you quite obviously did) path you have 150 treasure.")
    printWait("You can go 'LEFT', 'DOWN'")
    answer = getInput(["left", "down"])

    # If you go down, you die
    if answer.lower() == "down" or answer.lower() == "d":
        printWait("You found another treasure room")
        treasure = treasure + 30000
        printWait("This treasure room gained you " + str(treasure) +" treasure")

        printWait("However, as you picked up the treasure a hole in the floor appeared")
        printWait("You fell through the hole and died")
        lives = lives - 3
        input("Press any key to exit: ")
        exit()

    if answer.lower() == "left" or answer.lower() == "l":
        printWait("Well done you didn't die by going down the 'DOWN' path")
        printWait("For that you gain 50 treasure")
        treasure = treasure + 50
        printWait("You now have " + str(treasure) + " treasure")

    printWait("You may think that this is easy but it is not")
    printWait("This is because you have another path to walk down")
    printWait("'LEFT' or 'DOWN'")
    answer = getInput(["left", "down"])

    if answer.lower() == "down" or answer.lower() == "d":
        printWait("Well done, you chose the ......")
        printWait("Wrong path")
        printWait("You have died")
        printWait("Goodbye Hero")
        exit()

    if answer.lower() == "left" or answer.lower() == "l":
        printWait("Well done, you chose the ......")
        printWait("Correct Path")

    printWait("You now have to fight an ogre who really doesn't like the fact that you achieved this much within the game")
    printWait("You now have to choose between two options and if you survive you get to advance within the game")
    printWait("Choose option 'A' or option 'B'")
    answer = getInput(["a", "b"])
    if answer.lower() == "a":
        printWait("Well done you chose the ...")
        printWait("Correct Path")
        treasure = treasure + 50
        printWait("You now have " + str(treasure) + " treasure")
        printWait("However, the ogre doesnt like that you have almost escaped his fierce green hairy hands")

        printWait("He has challenged you to a number guessing game")
        ogreGame()
    else:
        printWait("Well done, you chose the ......")

        printWait("Incorrect path")
        input("Press any key to exit: ")
        exit()

# Path code from the start
elif answer.lower() == "right" or answer.lower() == "r":
    lives = 0
    printWait("A tiger jumps at you and scrapes your eyes off")
    printWait("Goodbye hero, there's no saving you...")
    input("Press any key to exit: ")
    exit()
elif answer.lower() == "down" or answer.lower() == "d":
    printWait("You are walking through the woods and see an old lady on the floor")
    printWait("You also have two paths to go down")
    printWait("You also have to choose option 'A' or 'B' ")
    printWait("However you do not get to see what happens between option 'A' or 'B' so choose very wisely")
    answer = getInput(["a", "b"])
    if answer.lower() == "a":
        printWait("You walked down the path with the old lady")

        printWait("You approach the old lady")

        printWait("You are now killed by the old lady because she turns out to be a witch")

        input("Press any key to exit: ")
        exit()
    elif answer.lower() == "b":
        printWait("You have walked down the second path away from the old lady")

        printWait("You chose the correct way because the old lady turnd out to be a witch so when you walked past her she would have killed you")

        treasure = treasure + 150
        printWait("For that you have gained 150 treasure. You now have " +str(treasure) + "treasure")
        printWait("You now have three more choices to make")
        answer = getInput(["left", "right", "down"])
        if answer.lower() == "r" or answer.lower() == "right":
            printWait("You keep walking forwards until you trip over a branch")
            printWait("You notice that there is a lever under a bush nearby as you get up")
            printWait("Do you pull the lever?")
            answer = askYesOrNo()
            if answer:
                printWait("A trapdoor opens up through which you decide to go through")
                printWait("You climb down into the medieval sewer system and find a golden ring")
                printWait("You put it on and find out that you can now breathe underwater")
                printWait("Do you swim in the sewers?")
                answer = askYesOrNo()
                if answer:
                    printWait("You jump down into the sewers and clench your nose as you swim")
                    printWait("You quickly dunk to see if there is anything inside the sewer")
                    printWait("You then realise that you can breathe underwater, but you are not immune to diseases")
                    printWait("You climb out of the sewer and lie down on your side")
                    printWait("You die a slow, painful death of cholera")
                    input("Press any key to exit: ")
                    exit()
                else:
                    printWait("You keep walking for miles and miles through the sewers")
                    printWait("Eventually you meet the secret underground sewer society (USUS) ran by Bruce Lee")
                    printWait("They treat you nicely and offer you food")
                    printWait("But they are not truly this nice...")
                    printWait("They are following one of their ancient cannibalist rituals and are stuffing you with raw rat meat")
                    printWait("They kill you and make stew from your toenails")
                    input("Press any key to exit: ")
                    exit()
            else:
                printWait("You correctly chose not to pull the lever")
                printWait("It would've opened the sewers and you would've either died of cholera poisoning or been eaten by the sewer people")

                quiz(currentQuiz)
                currentQuiz = currentQuiz + 1

                treasure = treasure + 300
                printWait("You gained 300 treasure for that you now have " +
                          str(treasure) + " treaure")

                # TODO
        elif answer.lower() == "d" or answer.lower() == "down":
            # TODO
            print()
        elif answer.lower() == "l" or answer.lower() == "left":
            # TODO
            print()
