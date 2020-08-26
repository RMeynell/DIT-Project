##
# dit_project.py
# created by: Regan Meynell

# import random
import random

# creating a menu system to navigate the program
def menu():
    user_choice = 11
    while user_choice <= 0 or user_choice >= 4:
        try:
            user_choice = int(input("""------------------------
Please choose an option:
(1). Basic Questions
(2). Hard Questions
(3). History
(4). Exit the game\n------------------------\n"""))
        except ValueError:
            print("Please enter a number")
    if user_choice == 1:
        basic_questions()
    elif user_choice == 2:
        hard_questions()
    elif user_choice == 3:
        history()
    elif user_choice == 4:
        print("Quitting")

# defining the function that will ask questions
def basic_questions():
    score = 0
    # asking the user what operation they would like to use
    operations = ["1", "2", "3"]
    operation = 0
    while operation not in operations:
        try:
            operation = input("""------------------------
What operation would you like to use:
(1). Addition,
(2). Subtraction,
(3). Multiplication?\n------------------------\n""").lower().strip()
        except ValueError:
            print("Please enter a number between 1 and 4")

    OP_SYMBOLS = ["+", "-", "x"]
    if operation == "1":
        operation = OP_SYMBOLS[0]
    elif operation == "2":
        operation = OP_SYMBOLS[1]
    elif operation == "3":
        operation = OP_SYMBOLS[2]
    # defining a dict to store previous questions the user has answered
    prev_answers = {
        }
    # asking the user how many questions they would like
    user_question = -1
    while user_question <= 0 or user_question > 50:
        try:
            user_question = int(input("How many questions would you like?\n"))
        except ValueError:
            print("Please enter a number above 0 and below 50")

    # creating a loop that will ask the user their given amount of questions
    for i in range(0, user_question):
        number1 = random.randint(0, 12)
        number2 = random.randint(0, 12)
        # preventing negative numbers
        while number1 < number2:
            number1 = random.randint(0, 12)
            number2 = random.randint(0, 12)
        # asking the user the questions
        question_num = (i + 1)
        user_answer = 0
        while user_answer == 0:
            try:
                user_answer = int(input("Question {}: {} {} {}\n= "
                .format(question_num, number1, operation, number2)))
            except ValueError:
                print("Please input a number value")
        prev_answers["{} {} {}".format(number1, operation, number2)] = ["{}".format(user_answer)]
        # checking if the users answer is correct
        if operation == "+":
            answer = number1 + number2
        elif operation == "-":
            answer = number1 - number2
        elif operation == "x":
            answer = number1 * number2
        if user_answer == answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
        user_answer = 0
    print("Your final score is {}/{}".format(score, user_question))
    menu = input("Would you like to return to the menu?\n").strip().lower()
    if menu == "yes":
        print("Returning to the menu")
        main()
    else:
        print("Quitting")

# defining function to give the user harder questions
def hard_questions():
    # setting score variable
    score = 0
    # asking the user what operation they would like to use
    OPERATIONS = ["1", "2", "3"]
    operation = 0
    while operation not in OPERATIONS:
        try:
            operation = input("""------------------------
What operation would you like to use:
(1). Addition,
(2). Subtraction,
(3). Multiplication?\n------------------------\n""").lower().strip()
        except ValueError:
            print("Please enter a number between 1 and 4")

    OP_SYMBOLS = ["+", "-", "x"]
    if operation == "1":
        operation = OP_SYMBOLS[0]
    elif operation == "2":
        operation = OP_SYMBOLS[1]
    elif operation == "3":
        operation = OP_SYMBOLS[2]
    # asking the user how many questions they would like
    user_question = -1
    while user_question <= 0 or user_question > 50:
        try:
            user_question = int(input("How many questions would you like?\n"))
        except ValueError:
            print("Please enter a number above 0 and below 50")
    # creating a loop that will ask the user their given amount of questions
    for i in range(0, user_question):
        number1 = random.randint(0, 24)
        number2 = random.randint(0, 24)
        # preventing negative numbers
        while number1 < number2:
            number1 = random.randint(0, 24)
            number2 = random.randint(0, 24)
        # asking the user the questions
        question_num = (i + 1)
        user_answer = 0
        while user_answer == 0:
            try:
                user_answer = int(input("Question {}: {} {} {}\n= "
                .format(question_num, number1, operation, number2)))
            except ValueError:
                print("Please input a number value")
        # checking if the users answer is correct
        if operation == "+":
            answer = number1 + number2
        elif operation == "-":
            answer = number1 - number2
        elif operation == "x":
            answer = number1 * number2
        if user_answer == answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    print("Your final score is {}/{}".format(score, user_question))
    menu = input("Would you like to return to the menu?\n").strip().lower()
    if menu == "yes":
        main()

#defining history function
def history():
    print("History")

# defining function main to start the program
def main():
    menu()

main()
