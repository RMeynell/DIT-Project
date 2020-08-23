##
# dit_project.py
# created by: Regan Meynell

#import random
import random

#creating a menu system to navigate the program
def menu():
    user_choice = 11
    while user_choice != 1 and user_choice != 2:
        try:
            user_choice = int(input("""Please choose an option:
(1). Basic Questions
(2). Hard Questions
(3). Choose your own questions\n"""))
        except ValueError:
            print("Please enter a number")
    if user_choice == 1:
        basic_questions()
    elif user_choice == 2:
        hard_questions()
    else:
        print("end")
       

#defining the function that will ask questions
def basic_questions():
    score = 0
    #asking the user what operation they would like to use
    operations = ["1", "2", "3"]
    operation = 0
    while operation not in operations:
        try:
            operation = input("""What operation would you like to use:
(1). Addition,
(2). Subtraction,
(3). Multiplication?\n:""").lower().strip()
        except ValueError:
            print("Please enter a number between 1 and 4")
            
    OP_SYMBOLS = ["+", "-", "x"]
    if operation == "1":
        operation = OP_SYMBOLS[0]
    elif operation == "2":
        operation = OP_SYMBOLS[1]
    elif operation == "3":
        operation = OP_SYMBOLS[2]
    #asking the user how many questions they would like
    user_question = -1
    while user_question <= 0:
        try:
            user_question = int(input("How many questions would you like?\n"))
        except ValueError:
            print("Please enter a number above 0")
    #creating a loop that will ask the user their given amount of questions
    for i in range(0, user_question):
        number1 = random.randint(0,12)
        number2 = random.randint(0,12)
        #not allowing negative numbers in the basic questions
        if operation == "2":
            if number1 > number2:
                user_answer = int(input("What is {} {} {}?\n".format(number2, operation, number1)))
            else:
                user_answer = int(input("What is {} {} {}?\n".format(number1, operation, number2)))
        user_answer = int(input("{} {} {}\n= ".format(number1, operation, number2)))
        #checking if the users answer is correct
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

#defining function to give the user harder questions
def hard_questions():
    #setting score variable
    score = 0
    #asking the user what operation they would like to use
    OPERATIONS = ["1", "2", "3"]
    operation = 0
    while operation not in operations:
        try:
            operation = input("""What operation would you like to use:
(1). Addition,
(2). Subtraction,
(3). Multiplication?\n:""").lower().strip()
        except ValueError:
            print("Please enter a number between 1 and 4")
            
    OP_SYMBOLS = ["+", "-", "x"]
    if operation == "1":
        operation = OP_SYMBOLS[0]
    elif operation == "2":
        operation = OP_SYMBOLS[1]
    elif operation == "3":
        operation = OP_SYMBOLS[2]
    #asking the user how many questions they would like
    user_question = int(input("How many questions would you like?\n"))
    #creating a loop that will ask the user their given amount of questions
    for i in range(0, user_question):
        number1 = random.randint(0,24)
        number2 = random.randint(0,24)
        user_answer = int(input("What is {} {} {}?\n".format(number1, operation, number2)))
        #checking if the users answer is correct
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

#defining function main to start the program
def main():
    menu()

main()
