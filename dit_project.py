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
    while user_choice <= 0 or user_choice >= 4:
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
        questions(prev_answers)
    elif user_choice == 2:
        history(prev_answers)
    elif user_choice == 3:
        user_info(name)
    elif user_choice == 4:
        print("Quitting...")
    return name

# defining the function that will ask questions
def questions(prev_answers):
    #setting the number of coins the user has
    coins = 10
    #setting continuous answer streak
    streak = 0
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
            coins += 5
            streak += 1
        else:
            print("Incorrect")
            streak = 0
        #giving the user a reward for having a streak
        if streak == 5:
            streak
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
   
# defining function for the gambling part of the program
def gamble():
    print("ghe")

# defining function to store the users info
def user_info(name):
    print("Name: {}".format(name))
    print("Coins: {}".format(coins))
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





"""
def questions():
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
    OPERATIONS = [+, -, /, *]
    random_op = random.randint(0,3)
    final_op = OPERATIONS[random_op]
    # asking the user the questions
    for i in range(0, 5):
    # setting the number range
    if difficulty = 1:
        number1 = random.randint(0, 12)
        number2 = random.randint(0, 12)
    else:
        number1 = random.randint(0, 24)
        number2 = random.randint(0, 24)
    #preventing negative numbers
        while number1 < number2:
            number1 = random.randint(0, 12)
            number2 = random.randint(0, 12)
"""



"""
import random

def questions():
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
    OPERATIONS = ["+", "-", "/", "*"]
    random_op = random.randint(0,3)
    final_op = OPERATIONS[random_op]
    # asking the user the questions
    for i in range(0, 5):
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
        #preventing negative numbers
        while number1 < number2:
            number1 = random.randint(0, 24)
            number2 = random.randint(0, 24)
        #asking the user the question
        question_num = (i + 1)
        user_answer = float(input("Question {}: {} {} {}\n= "
        .format(question_num, number1, final_op, number2)))
        #checking the answer
        answer = (number1, final_op, number2)
        if user_answer == answer:
            print("Correct")
        print(answer)
questions()
"""
