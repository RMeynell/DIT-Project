##
# new_code.py
# created by Regan Meynell

# importing random
import random

# defining variables
prev_answers = []
coins = 0
streak = 0
high_streak = 0
name = input("What is your Username?: ")
# defining function for the menu system
def menu(coins, prev_answers, name, streak, high_streak):
    user_choice = 11
    while user_choice <= 0 or user_choice >= 6:
        try:
            user_choice = int(input("""
------------------------
Please choose an option:
(1). Questions
(2). History
(3). User Info
(4). Program Info
(5). Quit Program
------------------------
"""))
        except:
            print("Please enter an integer between 1 and 5")

    # calling the correct function
    if user_choice == 1:
        difficulty_select(coins, prev_answers, streak, high_streak)
    elif user_choice == 2:
        history(prev_answers, streak, high_streak)
    elif user_choice == 3:
        user_info(name, coins, streak, high_streak)
    elif user_choice == 4:
        info()
    elif user_choice == 5:
        print("Quitting...")
    
# defining function to let the user choose their difficulty
def difficulty_select(coins, prev_answers, streak, high_streak):
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
        easy_questions(coins, prev_answers, streak, high_streak)
    elif difficulty == 2:
        hard_questions(coins, prev_answers, streak, high_streak)
        
# defining function to ask the user easy questions
def easy_questions(coins, prev_answers, streak, high_streak):
    questionfive = 0
    earned_coins = 0
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
                earned_coins += 10
                streak += 1
                questionfive += 1
            else:
                print("Incorrect")
                streak = 0
        elif operation == "-":
            answer = num1 - num2
            if user_answer == answer:
                print("Correct!")
                coins += 10
                earned_coins += 10
                questionfive += 1
                streak += 1
            else:
                print("Incorrect")
                streak = 0
        # checking if the users streak can give them a reward
        streak_prize = streak * 3
        if streak % 5 == 0 and streak > 0:
            print("You got a streak prize")
            print("Your streak reached {}".format(streak))
            print("This gives you a {} coin prize".format(streak_prize))
            coins += streak_prize
        # adding the users answer to the prev questions list
        question = "{} {} {}".format(num1, operation, num2)
        list_ans = "You answered: {}, the correct answer is: {}".format(user_answer, answer)
        prev_answers.append(question)
        prev_answers.append(list_ans)
    print("You got {}/5 correct".format(questionfive))
    print("You earned {} coins".format(earned_coins))
    # checking if the users highest streak has been beaten
    if streak > high_streak:
        high_streak = streak
    # returning the user to the menu if they would like
    menu_return(coins, prev_answers, name, streak, high_streak)
    return streak 
    
# defining function to ask the user hard questions
def hard_questions(coins, prev_answers, streak, high_streak):
    questionfive = 0
    earned_coins = 0
    # asking the user the question
    for i in range(0, 5):
        # generating random numbers
        num1 = random.randint(10, 24)
        num2 = random.randint(10, 24)
        # preventing negative numbers
        while num2 > num1:
            num1 = random.randint(10, 24)
            num2 = random.randint(10, 24)
        # generating random operations
        operation = random.randint(0, 2)
        if operation == 0:
            operation = "+"
        elif operation == 1:
            operation = "-"
        else:
            operation = "x"
        question_num = (i + 1)
        user_answer = int(input("Question {}: {} {} {} \n="
                                .format(question_num, num1, operation, num2)))
        # checking the answer
        if operation == "+":
            answer = num1 + num2
            if user_answer == answer:
                print("Correct!")
                coins += 20
                earned_coins += 20
                questionfive += 1
                streak += 1
            else:
                print("Incorrect")
                streak = 0
        elif operation == "-":
            answer = num1 - num2
            if user_answer == answer:
                print("Correct!")
                coins += 20
                earned_coins += 20
                questionfive += 1
                streak += 1
            else:
                print("Incorrect")
                streak = 0
        elif operation == "x":
            answer = num1 * num2
            if user_answer == answer:
                print("Correct!")
                coins += 20
                earned_coins += 20
                questionfive += 1
                streak += 1
            else:
                print("Incorrect")
                streak = 0
        # checking if the users streak can give them a reward
        streak_prize = streak * 2
        if streak % 5 == 0 and streak > 0:
            print("You got a streak prize")
            print("Your streak reached {}".format(streak))
            print("This gives you a {} coin prize".format(streak_prize))
            coins += streak_prize
        # adding the users answer to the prev questions list
        question = "{} {} {}".format(num1, operation, num2)
        prev_answers.append(question)
    print("You got {}/5 correct".format(questionfive))
    print("You earned {} coins".format(earned_coins))
    # checking if the users highest streak has been beaten
    if streak > high_streak:
        high_streak = streak
    menu_return(coins, prev_answers, name, streak, high_streak)
        
# defining function to view history
def history(prev_answers, streak, high_streak):
    answerlen = (len(prev_answers) / 2)
    int(answerlen)
    if len(prev_answers) == 0:
        print("There are no available questions to view")
        print("Returning to the menu")
        menu(coins, prev_answers, name, streak, high_streak)
    else:
        print("There are {} total questions available to view".format(answerlen))
        view_num = int(input("How many questions would you like to view? \n"))
        view_num = view_num * 2
        view_num = "-{}".format(view_num)
        new_num = int(view_num)
    # printing the wanted number of questions
    for i in range(new_num, 0):
        print(prev_answers[i])
        
# defining function to view user info
def user_info(name, coins, streak, high_streak):
    print("Username: {}".format(name))
    print("You currently have {} coins".format(coins))
    print("Your highest streak is: {}".format(high_streak))
    print("Your current streak is: {}".format(streak))
    # returning users to the menu
    menu_return(coins, prev_answers, name, streak, high_streak)

# defining function to allow the user to quit the program
def menu_return(coins, prev_answers, name, streak, high_streak):
    # returning the user to the menu if they would like
    back = -1
    while back <= 0 or back >= 3:
        try:
            back = int(input("""
-------------------------------------
Would you like to return to the menu:
(1). Yes
(2). No
-------------------------------------
"""))
        except:
            print("Please enter 1 or 2")
    if back == 1:
        print("Returning to the menu")
        menu(coins, prev_answers, name, streak, high_streak)
    else:
        print("Quitting...")

# defining function to give the user information about the program
def info():
    print("""
------------------------------------------------------------------------
                               Questions:
     You will be given a set of questions at your chosen difficulty
            The two difficulties available are easy and hard
            Easy gives you addition and subtraction questions
The easy questions will use randomly generated numbers between 0 and 12
   Hard gives you addition, subtraction, and multiplication questions
The hard questions will use randomly generated numbers between 10 and 24
------------------------------------------------------------------------
                                 Coins:
     For every easy question you get correct you will earn 10 coins
     For every hard question you get correct you will earn 10 coins
      You also get a reward for getting consecutive correct answers
              Every time your streak passes a multiple of 5
                   You will earn 2 times the multiple
------------------------------------------------------------------------
                                History:
     This screen shows you the previous questions you have answered
       You can choose how many of these question it will show you
         It will also tell you if you were correct or incorrect
------------------------------------------------------------------------
                               User Info:
                   This screen displays your user name,
           your current amount of coins, your current streak,
                         and your highest streak
------------------------------------------------------------------------""")
    menu_return(coins, prev_answers, name, streak, high_streak)      
# defining function main to start the program
def main():
     menu(coins, prev_answers, name, streak, high_streak)

main()
