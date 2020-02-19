import time

print("This file is a series of mini programs I made while learning Python.")
print("Please select a program from the following list.\n")
print("'1' for Square Sequence.")
print("'2' for Macro to Calorie Calculator.")
print("'3' for Random Name Generator.")
print("'4' for Hangman.\n")
           
prog = int(input("Insert ID for the program you wish to use: "))

if (prog == 1):
    print("\nThe following program takes a number and increments it by 1")
    print("part of a for loop. Each number in the sequence will have its")
    print("square value displayed.")
    print("The sequence will end when the square number exceeds 200.\n")
    x = 0
    start_num = int(input("Insert number you wish to start the sequence: "))



    for x in range(100):
        square_number = start_num*start_num
        if (square_number < 200):
            print(str(start_num), end = ' ')
            print("When squared equals: " + str(square_number))
            start_num += 1


if (prog == 2):
    print("\nThe following program converts protein, fat and carbs into calories.")
    print("Please insert in g the quantity of these macros.\n")
    protein = int(input("Insert protein in g: "))
    fat = int(input("Insert fat in g: "))
    carbs = int(input("Insert carb in g: "))
    calories = (protein*4)+(fat*9)+(carbs*4)
    print("\n" + str(calories) + " kcals or " + str(calories*4.184) + "kj")
    

if (prog == 3):
    repeat = "y"
    print("\nThe following program selects a random name from a pool")
    print("drawn from a text file.\n")
    print("Please select gender.")
    import random
    gender = str(input("1 for Male or 2 for Female: "))
    if (gender == "1"):
        while (repeat == "y"):
            name_file = open("male_name.txt").readlines() 
            name_pull = name_file[random.randint(1,1001)]

            names_list = name_pull.split()
            chosen_name = random.choice(names_list)
            print("\n" + chosen_name)
            repeat = str(input("\nTry again (y/n)?: "))
    elif (gender == "2"):
        while (repeat == "y"):
            name_file = open("female_name.txt").readlines() 
            name_pull = name_file[random.randint(1,1001)]

            names_list = name_pull.split()
            chosen_name = random.choice(names_list)
            print("\n" + chosen_name)
            repeat = str(input("\nTry again (y/n)?: "))

    
if (prog == 4):
    import random
    known = False
    word_file = open("hangman_pool.txt").readlines()
    word_pull = word_file[random.randint(1,116)]

    word_list = word_pull.split()
    cwrd = list(random.choice(word_list))
    p = list("________")

    char_1 = cwrd[0]
    char_2 = cwrd[1]
    char_3 = cwrd[2]
    char_4 = cwrd[3]
    char_5 = cwrd[4]
    char_6 = cwrd[5]
    char_7 = cwrd[6]
    char_8 = cwrd[7]

    your_1 = p[0]
    your_2 = p[1]
    your_3 = p[2]
    your_4 = p[3]
    your_5 = p[4]
    your_6 = p[5]
    your_7 = p[6]
    your_8 = p[7]

    attempts = 8

    while (known == False)&(attempts > 0):
        print(p)
        print("Attempts remaining: " + str(attempts))
        answer = cwrd
        guess = str(input("Do you know the word (y/n)?: "))
        if (guess == "y"):
            guess = str(input("What's your call?: "))
            if (guess == answer):
                p == cwrd
                print(answer)
                print("SUCCESS")
                
                known = True
            else:
                print("FAILURE")
                attempts-=1
        elif (guess == "n"):
            guess = str(input("Pick a letter: "))
            attempts-=1
            if (guess == char_1):
                p[0] = cwrd[0]   
            if (guess == char_2):    
                p[1] = cwrd[1]
            if (guess == char_3):    
                p[2] = cwrd[2]
            if (guess == char_4):    
                p[3] = cwrd[3]
            if (guess == char_5):    
                p[4] = cwrd[4]
            if (guess == char_6):    
                p[5] = cwrd[5]
            if (guess == char_7):    
                p[6] = cwrd[6]
            if (guess == char_8):    
                p[7] = cwrd[7]
            if (p == cwrd):
                print("YOU WIN")
                known = True
            if (attempts == 0):
                print("YOU LOSE!")
            



print("\nTest ended, Python will close in 5 seconds")
time.sleep(5)
