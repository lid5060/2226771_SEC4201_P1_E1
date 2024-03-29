# try is being used to try and run the code if an integer is not used then an error will occur which we be displayed
# to the user and the programme will loop error handling is broken again fix it!!!! when implemented above and below choice = int
# it either says that it isn't referenced or it just skips past
# the error handling now seems to be working - testing has been completed and the issue was just wrapping the choice = int in the try loop
# instead of the whole code block
while True:
    print("Welcome to the programme\n")
    print("Enter a number between 1 - 9 to pick which question to go to or enter 0 to exit\n")
    try:
        choice = int(input())
        if choice < 0:
            print("Please enter a valid number")
        elif choice > 9:
            print("Please enter a valid number")
        elif choice == 1:
# defining the variables where the users name will be stored
            first_name = input("Please enter your first name\n")
            last_name = input("Please enter your last name\n")
            print("Hello, " + first_name + " " + last_name)
# question one has been implemented and after some testing has proved to be working without issues
        elif choice == 2:
            print("Press enter to see the answer\n")
            input("What do you hear if you put the Linux Shell to your ear?\n")
            print("The C")
        elif choice == 3:
                print("Enter 2 numbers to add together and then a third to multiply by\n")
# the user inputs all three number which are stored and then the first numbers are added together and stored in first_total
# then they are multiplied in total and then are printed to the screen
                num1 = int(input("Please enter the first number\n"))
                num2 = int(input("Please enter the second number\n"))
                num3 = int(input("Please enter the third number\n"))
                first_total = num1 + num2
                total = first_total * num3
                print("your total is", total)
        elif choice == 4:
            slice_start = int(input("How many slices of pizza did you start with?\n"))
            slice_eaten = int(input("How many slices have you eaten?\n"))
            slices_left: int = slice_start - slice_eaten
            if slice_start > slice_eaten:
                print("You have", slices_left, "slices of pizza left\n")
# the code below will make it so if the user inputs that they have eaten more pizza slices than they started with they will receive an error message
# and go back to the start
            elif slice_start < slice_eaten:
                print("You must have entered the wrong numbers try again\n")
# the age wouldn't print out with the name and after some testing and thinking I remembered I had to set it to an int or float
# for it to print out the number
        elif choice == 5:
            name = input("Please enter your first name\n")
            age = int(input("Please enter your age\n"))
            new_age = age + 1
            print(name, "next birthday you will be", new_age)
        elif choice == 6:
            bill_total = float(input("What is the total price of the bill?\n"))
            diners_total = int(input("How many diners are there?\n"))
            price_per_diner = bill_total / diners_total
            print("Each person must pay", price_per_diner)
        elif choice == 7:
            weight = float(input("Please enter your weight in kilograms\n"))
            pounds = weight * 2.204
            print("Your weight in pounds is", pounds)
        elif choice == 8:
            num1 = int(input("Please enter in the first number\n"))
            num2 = int(input("Please enter in the number you want to divide by\n"))
            divided_num = num1 // num2
            remainder_num = num1 % num2
# we work out the first number when divided, and then we work out the remainder to print out to the user
            if num1 > num2:
                print(num1, "divided by", num2, "is", divided_num, "with a remainder of", remainder_num)
# an error will be printed to the user if they input a number for the second one which is higher than the first
            elif num1 < num2:
                print("Error second number cant be higher than the first try again")
        elif choice == 9:
            print("Name of a shape by entering the number of sides")
            shape_sides = int(input("Please enter a number between 3 - 10 to see the name of the shape\n"))
            if shape_sides == 3:
                print("Your shape is called a triangle\n")
            elif shape_sides == 4:
                print("Your shape is called a quadrilateral\n")
            elif shape_sides == 5:
                print("Your shape is called a pentagon\n")
            elif shape_sides == 6:
                print("Your shape is called a hexagon\n")
            elif shape_sides == 7:
                print("Your shape is called a heptagon\n")
            elif shape_sides == 8:
                print("Your shape is called a octagon\n")
            elif shape_sides == 9:
                print("Your shape is called a nonagon\n")
            elif shape_sides == 10:
                print("Your shape is called a decagon\n")
            elif shape_sides < 3:
                print("Please enter a number between 3 - 10\n")
            elif shape_sides > 10:
                print("Please enter a number between 3 - 10\n")
        elif choice == 0:
            break
    except Exception:
        print("Error please enter a number")
# all questions and the code for them need to be implemented along with error handling for all the inputs as completed above
# if the user inputs a number which is lower than or equal to 0 they will be sent back to the start of the programme with an error message

# bibliography
# Ghadge, D., 2023. Building a Command-Line Menu in Python: Exploring Different Applications. [Online]
# Available at: https://medium.com/@dghadge2002/building-a-command-line-menu-in-python-exploring-different-applications-f970a61e6412
# [Accessed 1 March 2024]
# w3schools, n.d. Python Try Except. [Online]
# Available at: https://www.w3schools.com/python/python_try_except.asp
# [Accessed 1 March 2024]
# Bob, 2011. Find the division remainder of a number. [Online]
# Available at: https://stackoverflow.com/questions/5584586/find-the-division-remainder-of-a-number
# [Accessed 4 March 2024]