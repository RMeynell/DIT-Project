##
# dit_project.py
# created by: Regan Meynell

#import random
import random

#defining the function that will ask questions
def questions():
    score = 0
    addition = "+"
    subtraction = "-"
    multiplication = "x"
    #asking the user what operation they would like to use
    operation = input("""What operation would you like to use:
Addition,
Subtraction,
Multiplication?\n""").lower().strip()
    #running the right operation
    if operation == "addition":
        #starting a loop that will ask the user questions
        for i in range(0, 5):
            number1 = random.randint(0,12)
            number2 = random.randint(0,12)
            answer = int(input("What is {} + {}?\n".format(number1, number2)))
            #checking if the users answer is correct
            if answer == number1 + number2:
                print("Correct")
                score += 1
            else:
                print("That is incorrect")
        print("Your final score is: {}/5".format(score))
    elif operation == "subtraction":
        #starting a loop that will ask the user questions
        for i in range(0, 5):
            number1 = random.randint(0,12)
            number2 = random.randint(0,12)
            answer = int(input("What is {} - {}?\n".format(number1, number2)))
            #checking if the users answer is correct
            if answer == number1 - number2:
                print("Correct")
                score += 1
            else:
                print("That is incorrect")
        print("Your final score is: {}/5".format(score))
    elif operation == "multiplication":
        #starting a loop that will ask the user questions
        for i in range(0, 5):
            number1 = random.randint(0,12)
            number2 = random.randint(0,12)
            answer = int(input("What is {} x {}?\n".format(number1, number2)))
            #checking if the users answer is correct
            if answer == number1 * number2:
                print("Correct")
                score += 1
            else:
                print("That is incorrect")
        print("Your final score is: {}/5".format(score))

        
questions()












        
        
        
    
