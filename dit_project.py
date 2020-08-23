##
# dit_project.py
# created by: Regan Meynell

#import random
import random

#creating a menu system to navigate the program
def menu():
    user_choice = 11
    while user_choice != 1 and user_choice != 2:
        user_choice = int(input("""Please choose an option:
(1). Basic Questions
(2). Hard Questions
(3). Choose your own questions\n"""))
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
    operation = input("""What operation would you like to use:
Addition,
Subtraction,
Multiplication?\n""").lower().strip()
    #setting operation to the correct symbol
    if operation == "addition":
        operation = "+"
    elif operation == "subtraction":
        operation = "-"
    elif operation == "multiplication":
        operation = "x"
    #asking the user how many questions they would like
    user_question = int(input("How many questions would you like?\n"))
    #creating a loop that will ask the user their given amount of questions
    for i in range(0, user_question):
        number1 = random.randint(0,12)
        number2 = random.randint(0,12)
        user_answer = int(input("What is {} {} {}?\n".format(number1, operation, number2)))
        #checking if the users answer is correct
        if operation == "+":
            if user_answer == number1 + number2:
                print("Correct")
                score += 1
            else:
                print("Incorrect")
        elif operation == "-":
            if user_answer == number1 - number2:
                print("Correct")
                score += 1
            else:
                print("Incorrect")
        elif operation == "x":
            if user_answer == number1 * number2:
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
    print("end")

#defining function main to start the program
def main():
    menu()

main()











        
        
        
    
