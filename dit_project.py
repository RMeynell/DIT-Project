##
# dit_project.py
# created by: Regan Meynell

# import random
import random

# asking the user for their name
name = input("What is your name?\n")
# defining dict to store users previous questions
prev_answers = {
    
    }
    
# creating a menu system to navigate the program
def menu(name):
    user_choice = 11
    while user_choice <= 0 or user_choice >= 5:
        try:
            user_choice = int(input("""------------------------
Please choose an option:
(1). Questions
(2). History
(3). View Your Info
(4). Exit the game\n------------------------\n"""))
        except ValueError:
            print("Please enter a number")
    if user_choice == 1:
        final_coins = questions(prev_answers)
    elif user_choice == 2:
        history(prev_answers)
    elif user_choice == 3:
        user_info(name, final_coins)
    elif user_choice == 4:
        print("Quitting...")
    return name

def questions(prev_answers):
    coins = 0
    streak = 0
    # setting difficulty
    difficulty = -1
    while difficulty != 1 and difficulty != 2:
        try:
            difficulty = int(input("""------------------------
What difficulty would you like?
(1). Easy
(2). Hard\n------------------------\n"""))
        except:
            print("Please enter 1 or 2")
    # randomnizing the operation
    OPERATIONS = ["+", "-", "*"]
    random_op = random.randint(0,2)
    final_op = OPERATIONS[random_op]
    # asking the user the questions
    for i in range(0, 2):
        # setting the number range
        if difficulty == 1:
            number1 = random.randint(0, 12)
            number2 = random.randint(0, 12)
        #preventing negative numbers
        while number1 < number2:
            number1 = random.randint(0, 12)
            number2 = random.randint(0, 12)
        else:
            number1 = random.randint(0, 24)
            number2 = random.randint(0, 24)
        #asking the user the question
        question_num = (i + 1)
        user_answer = float(input("Question {}: {} {} {}\n= "
        .format(question_num, number1, final_op, number2)))
        #checking the answer
        if final_op == "+":
            answer = number1 + number2
        elif final_op == "-":
            answer = number1 - number2
        elif final_op == "x":
            answer = number1 * number2
        if user_answer == answer:
            print("You got it correct")
            coins += 10
            print("You got 10 coins")
            streak += 1
            print("Your current streak is: {}".format(streak))
        else:
            print("Incorrect")
            print("The correct answer was {}".format(answer))
            streak == 0
            print("Your current streak is: {}".format(streak))
    final_coins = coins
    print(final_coins)
    menu = "hello"
    while menu == "hello":
        menu = input("Would you like to return to the menu?\n").strip().lower()
        if menu == "yes":
            print("Returning to the menu")
            main()
        else:
            print("Quitting...")
    return final_coins

#defining history function
def history(prev_answers):
    #asking the user how many questions they would like to see
    if len(prev_answers) == 0:
        print("""
There are no questions available to view
Returning to the menu""")
        main()
    total_questions = len(prev_answers)
    print("There are a total of {} possible questions to view".format(total_questions))
    view_questions = int(input("How many of these questions would you like to view?\n"))
   
# defining function for the gambling part of the program
def gamble():
    print("ghe")

# defining function to store the users info
def user_info(name, final_coins):
    print("Name: {}".format(name))
    print("Coins: {}".format(final_coins))
    menu = input("Would you like to return to the menu?\n").strip().lower()
    if menu == "yes":
        print("Returning to the menu")
        main()
    else:
        print("Quitting...")

# defining function main to start the program
def main():
    menu(name)

main()
