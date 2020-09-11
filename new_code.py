##
# new_code.py
# created by Regan Meynell

# importing random
import random

# defining variables
prev_answers = {}
coins = 0
name = input("What is your Username? \n")
# defining function for the menu system
def menu(coins, prev_answers, name):
    user_choice = 11
    while user_choice <= 0 or user_choice >= 5:
        try:
            user_choice = int(input("""
------------------------
Please choose an option:
(1). Questions
(2). History
(3). User Info
(4). Quit Program
------------------------
"""))
        except:
            print("Please enter an integer between 1 and 4")

    # calling the correct function
    if user_choice == 1:
        difficulty_select(coins, prev_answers)
    elif user_choice == 2:
        history(prev_answers)
    elif user_choice == 3:
        user_info(name, coins)
    elif user_choice == 4:
        print("Quitting...")
    
# defining function to let the user choose their difficulty
def difficulty_select(coins, prev_answers):
    # asking the user what difficulty they would like
    difficulty = -1
    while difficulty <= 0 or difficulty >= 3:
        try:
            difficulty = int(input("""
---------------------------
Please choose a difficulty:
(1). Easy Questions
(2). Hard Questions
---------------------------
"""))
        except:
            print("Please enter 1 or 2")
    # calling the correct function
    if difficulty == 1:
        easy_questions(coins, prev_answers)
    elif difficulty == 2:
        hard_questions(coins, prev_answers)
        
# defining function to ask the user easy questions
def easy_questions(coins, prev_answers):
    questionfive = 0
    # asking the user the question
    for i in range(0, 5):
        # generating random numbers
        num1 = random.randint(0, 12)
        num2 = random.randint(0, 12)
        # preventing negative numbers
        while num2 > num1:
            num1 = random.randint(0, 12)
            num2 = random.randint(0, 12)
        # generating random operations
        operation = random.randint(0, 1)
        if operation == 0:
            operation = "+"
        else:
            operation = "-"
        question_num = (i + 1)
        user_answer = int(input("Question {}: {} {} {} \n="
                                .format(question_num, num1, operation, num2)))
        # checking the answer
        if operation == "+":
            answer = num1 + num2
            if user_answer == answer:
                print("Correct!")
                coins += 10
                questionfive += 1
            else:
                print("Incorrect")
        elif operation == "-":
            answer = num1 - num2
            if user_answer == answer:
                print("Correct!")
                coins += 10
                questionfive += 1
            else:
                print("Incorrect")
    print("You got {}/5 correct".format(questionfive))
    # adding the users answer to the prev questions dict
    prev_answers["Question: {} {} {}".format(num1, operation, num2)]\
    : "Your answer: {}, Correct answer: {}".format(user_answer, answer)

    # returning the user to the menu if they would like
    menu = input("Would you like to return to the menu?\n").strip().lower()
    if menu == "yes":
        menu(coins, prev_answers, name)
    else:
        print("Quitting...")

# defining function to ask the user hard questions
def hard_questions(coins, prev_answers):
    # generating random numbers
    num1 = random.randint(0, 24)
    num2 = random.randint(0, 24)
    # preventing negative numbers
    while number2 > number1:
        num1 = random.randint(0, 24)
        num2 = random.randint(0, 12)
    # generating random operations
    operation = random.randint(0, 2)
    if operation == 0:
        operation = "+"
    elif operation == 1:
        operation = "-"
    else:
        operation = "X"
    #asking the user the question
    for i in range(0, 5):
        question_num = (i + 1)
        user_answer = int(input("Question {}: {} {} {} \n="
                                .format(question_num, num1, operation, num2)))
    # checking the answer
    if operation == "+":
        answer = num1 + num2
        if user_answer == answer:
            print("Correct!")
            coins += 10
        else:
            print("Incorrect")
    elif operation == "-":
        answer = num1 - num2
        if user_answer == answer:
            print("Correct!")
            coins += 10
        else:
            print("Incorrect")
    elif operation == "X":
        answer = num1 * num2
        if user_answer == answer:
            print("Correct!")
            coins += 10
        else:
            print("Incorrect")
    # adding the users answer to the prev questions dict
    prev_answers["Question: {} {} {}".format(num1, operation, num2)]\
    : "Your answer: {}, Correct answer: {}".format(user_answer, answer)

    # returning the user to the menu if they would like
    menu = input("Would you like to return to the menu?\n").strip().lower()
    if menu == "yes":
        menu(coins, prev_answers, name)
    else:
        print("Quitting...")
        
# defining function to view history
def history():
    print("Hello")
# defining function to view user info
def user_info(name, coins):
    print("Username: {}".format(name))
    print("You currently have {} coins".format(coins))
    
# defining function main to start the program
def main():
     menu(coins, prev_answers, name)

main()
