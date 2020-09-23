##
# dit_project.py
# created by Regan Meynell

# importing random
import random

# defining variables
coins = 1000
streak = 0
high_streak = 0
user_items = ["", "", ""]
name = input("What is your Username?: ")

# defining function for the menu system

def menu(coins, name, streak, high_streak, user_items):
    user_choice = 11
    while user_choice <= 0 or user_choice >= 7:
        try:
            user_choice = int(input("""
------------------------
Please choose an option:
(1). Questions
(2). Gambling
(3). Shop
(4). User Info
(5). Program Info
(6). Quit Program
------------------------
"""))
        except:
            print("Please enter an integer between 1 and 4")

    # calling the correct function
    if user_choice == 1:
        difficulty_select(coins, name, streak, high_streak)
    elif user_choice == 2:
        gamble(coins, name, streak, high_streak)
    elif user_choice == 3:
        shop(coins, user_items)
    elif user_choice == 4:
        user_info(coins, name, streak, high_streak, user_items)
    elif user_choice == 5:
        info()
    elif user_choice == 6:
        print("Quitting...")
    
# defining function to let the user choose their difficulty
def difficulty_select(coins, name, streak, high_streak):
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
        easy_questions(coins, streak, high_streak)
    elif difficulty == 2:
        hard_questions(coins, streak, high_streak)
        
# defining function to ask the user easy questions
def easy_questions(coins, streak, high_streak):
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
        user_answer = 0.5
        while user_answer == 0.5:
            try:
                user_answer = int(input("Question {}: {} {} {} \n="
                                .format(question_num, num1, operation, num2)))
            except:
                print("Please enter an integer")
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
    menu(coins, name, streak, high_streak, user_items)
    return streak 
    
# defining function to ask the user hard questions
def hard_questions(coins, streak, high_streak):
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
        user_answer = 0.5
        while user_answer == 0.5:
            try:
                user_answer = int(input("Question {}: {} {} {} \n="
                                .format(question_num, num1, operation, num2)))
            except:
                print("Please enter an integer")
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
    menu(coins, name, streak, high_streak, user_items)
    return streak

# defining function for the gambling feature
def gamble(coins):
    if coins <= 29:
        print("You don't have enough coins")
        menu(coins, name, streak, high_streak, user_items)
    gamble = input("Would you like to gamble $30 (Y/N)").strip().lower()
    print(gamble)
    if gamble == "y":
        coins -= 30
        print("Generating a random number between 0 and 10,000")
        number = random.randint(0, 10000)
        number = 10000
        print("The random number was {}".format(number))
        if number < 5000:
            print("You won 20 coins")
            coins += 20
            menu(coins, name, streak, high_streak, user_items)
        elif number > 5000 and number < 8000:
            print("You won 30 coins")
            coins += 30
            menu(coins, name, streak, high_streak, user_items)
        elif number > 8000 and number < 9500:
            print("You won 50 coins")
            coins += 50
            menu(coins, name, streak, high_streak, user_items)
        elif number > 9500 and number < 9999:
            print("You won 100 coins")
            coins += 100
            menu(coins, name, streak, high_streak, user_items)
        elif number == 10000:
            print("You won 10,000 coins")
            coins += 10000
            menu(coins, name, streak, high_streak, user_items)

# defining function for the shop
def shop(coins, user_items):
    # defining variables
    shop_items = ["(1). Pencil", "(2). Blank Book", "(3). Calculator", "(4). Return to menu"]
    # showing the user items they can buy
    print("Welcome to the shop")
    print("You currently have {} coins".format(coins))
    print("--------------------------")
    for i in range(0, len(shop_items)):
        print(shop_items[i])
    print("--------------------------")
    # checking the user enough coins to buy their selected item
    price_met = False    
    while price_met == False:
        try:
            item_buy = int(input("Which item would you like to buy today?: \n"))
        except:
            print("Please enter a number between 1 and 4")
        if item_buy == 1 and coins >= 10:
            price_met = True
            print("You have successfuly bought a Pencil")
            coins -= 10
            shop_items.remove[0]
        elif item_buy == 2 and coins >= 30:
            price_met = True
            print("You have successfuly bought a Blank Book")
            book_no += 1
            user_items[0] = "{}x Blank Book".format(book_no)
            coins -= 30
            shop_items.remove[1]
        elif item_buy == 3 and coins >= 100:
            price_met = True
            print("You have successfuly bought a Calculator")
            calc_no += 1
            user_items[0] = "{}x Calculator".format(calc_no)
            coins -= 100
            shop_items.remove[2]
        elif item_buy == 4:
            menu(coins, name, streak, high_streak, user_items)
        else:
            print("You do not have enough coins to buy that item")
    # asking the user if they would like to return to the menu
    menu_return = -1
    while menu_return <= 0 or menu_return >= 3:
        try:
            menu_return = int(input("""
-----------------------------------------------
Would you buy more items or return to the menu?
(1). Return to the shop
(2). Return to the menu
-----------------------------------------------
"""))
        except:
            print("Please enter 1 or 2")
    if menu_return == 1:
        shop(coins, user_items)
    else:
        menu(coins, name, streak, high_streak, user_items)

# defining function to view user info
def user_info(coins, name, streak, high_streak, user_items):
    print("Username: {}".format(name))
    print("You currently have {} coins".format(coins))
    print("Your highest streak is: {}".format(high_streak))
    print("Your current streak is: {}".format(streak))
    view_inventory = "x"
    while view_inventory != "y" and view_inventory != "n":
        try:
            view_inventory = input("Would you like to view your inventory? (Y/N)").strip().lower()
        except:
            ("Please enter Y or N")
    if view_inventory == "y":
        for i in range(0, len(user_items)):
            print(user_items[i])
    # returning users to the menu
    menu(coins, name, streak, high_streak, user_items)

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
     For every hard question you get correct you will earn 20 coins
      You also get a reward for getting consecutive correct answers
              Every time your streak passes a multiple of 5
                   You will earn 2 times the multiple
------------------------------------------------------------------------
                               User Info:
                   This screen displays your user name,
           your current amount of coins, your current streak,
                         and your highest streak
------------------------------------------------------------------------""")
    menu(coins, name, streak, high_streak, user_items)      
# defining function main to start the program
def main():
    menu(coins, name, streak, high_streak, user_items)

main()
