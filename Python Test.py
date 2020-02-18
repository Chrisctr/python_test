print("This file is a series of mini programs I made while learning Python.")
print("Please select a program from the following list.\n")
print("'1' for Square Sequence.")
print("'2' for Macro to Calorie Calculator.\n") 
           
prog = int(input("Insert number the ID for the program you wish to use: "))

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
    print("\n" + str(calories))
    


