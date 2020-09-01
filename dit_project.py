##
# dit_project.py
# created by: Regan Meynell

# import random
import random

# defining dict to store users previous questions
prev_answers = {
    1 == ["Hello World"]
    }
    
# creating a menu system to navigate the program
def menu():
    user_choice = 11
    while user_choice <= 0 or user_choice >= 4:
        try:
            user_choice = int(input("""------------------------
Please choose an option:
(1). Questions
(2). History
(3). Exit the game\n------------------------\n"""))
        except ValueError:
            print("Please enter a number")
    if user_choice == 1:
        questions(prev_answers)
    elif user_choice == 2:
        history(prev_answers)
    elif user_choice == 3:
        print("Quitting...")

# defining the function that will ask questions
def questions(prev_answers):
    #asking the user what difficulty they would like
    difficulty = -1
    while difficulty != 1 and difficulty != 2:
        try:
            difficulty = int(input("""------------------------
What difficulty would you like?
(1). Easy
(2). Hard\n------------------------\n"""))
        except ValueError:
            print("Please enter 1 or 2")
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
    # asking the user how many questions they would like
    user_question = -1
    while user_question <= 0 or user_question > 50:
        try:
            user_question = int(input("How many questions would you like?\n"))
        except ValueError:
            print("Please enter a number above 0 and below 50")
    # creating a loop that will ask the user their given amount of questions
    for i in range(0, user_question):
        if difficulty == 1:
            number1 = random.randint(0, 12)
            number2 = random.randint(0, 12)
        elif difficulty == 2:
            number1 = random.randint(0, 24)
            number2 = random.randint(0, 24)
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
        #saving the users answer to a dictionary
        prev_answers[Question] = [number1, operation, number2, user_answer]
        user_answer = 0
    print("Your final score is {}/{}".format(score, user_question))
    menu = input("Would you like to return to the menu?\n").strip().lower()
    if menu == "yes":
        print("Returning to the menu")
        main()
    else:
        print("Quitting...")
    return prev_answers

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
    

# defining function main to start the program
def main():
    menu()

main()
