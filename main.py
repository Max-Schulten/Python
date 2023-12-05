import pandas
import random


db = pandas.read_csv('playerdb.csv')

attributesClassic = ["Pace", "Shooting", "Dribbling", "Passing", "Defending", "Physicality"]

attributesMedium = ["Finishing", "Strength", "Age", "Aggression"]

attributesHard = ["Jumping", "Composure", "Crossing"]


def playerdisplay(index):
    str = ""
    for column in db:
        str = str + f"{column}: {db[column][index]}, "

    print(str)
    mainmenu()


def search():
    print("Enter the player you want to search for.")
    name_input = input("")

    for i, name in enumerate(db["Name"]):
        if name == name_input:
            playerdisplay(i)


def mainloop(length, mode):
    score = 0

    if mode == "Classic":
        attribute = attributesClassic
        interval = 100
    elif mode == "Weird":
        attribute = attributesMedium
        interval = 250
    elif mode == "Weirdest":
        attribute = attributesHard
        interval = 500
    else:
        mainmenu()

    for i in range(length):
        index1 = random.randint(0, interval)
        index2 = random.randint(0, interval)
        attr = random.choice(attribute)
        p1 = (db["Name"][index1])
        p2 = (db["Name"][index2])
        p1attr = db[attr][index1]
        p2attr = db[attr][index2]

        print(f"Does {p1} have higher {attr} than {p2}?")
        guess = input("y/n?: ")
        if guess == 'y':
            if p1attr > p2attr:
                score += 1
                print("Correct!")
                print(f"{p1} has higher {attr} than {p2}!")
                print(f"Your current score is {score}.")

            else:
                print("Incorrect")
                print(f"{p1} has lower {attr} than {p2}!")
                print(f"Your current score is {score}.")
        else:
            if p1attr < p2attr:
                score += 1
                print("Correct!")
                print(f"{p1} has lower {attr} than {p2}!")
                print(f"Your current score is {score}.")
            else:
                print("Incorrect")
                print(f"{p1} has higher {attr} than {p2}!")
                print(f"Your current score is {score}.")
    print(f"Your final score after {length} rounds is {score}.")
    print(f"You were correct {(score / length) * 100}% of the time")


def mainmenu():
    print("Enter S for search, G for game.")
    if (input("") == "S"):
        search()
    print("Select a game mode: Classic, Weird, Weirdest, Custom")
    mode = input("")
    print(
        "Select how long you'd like to play. Enter E for endless gameplay or type any integer for a finite number of "
        "rounds")
    length = input("")
    if length == 'E':
        mainloop(9999, mode)
    else:
        mainloop(int(length), mode)


mainmenu()
