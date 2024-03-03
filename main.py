# try is being used to try and run the code if an integer is not used then an error will occur which we be displayed
# to the user and the programme will loop error handling is broken again fix it!!!! when implemented above and below choice = int it either says that it isn't referenced or it just skips past
# the error handling now seems to be working - testing has been completed and the issue was just wrapping the choice = int in the try loop instead of the whole code block
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
            input("What do you hear if you put the Linux Shell to your ear?\n")
            print("Press enter to see the answer\n")
            print("The C")
        elif choice == 3:
                print("Enter 2 numbers to add together and then a third to multiply by\n")
                num1 = float(input("Please enter the first number\n"))
                num2 = float(input("Please enter the second number\n"))
                num3 = float (input("Please enter the third number\n"))
# the user enters the numbers they want to add together, and then they enter the number they want to multiply by
                first_total = num1 + num2
                total = first_total * num3
                print("your total is", total)
        elif choice == 4:
            slice_start = int(input("How many slices of pizza did you start with?\n"))
            slice_eaten = int(input("How many slices have you eaten?\n"))
            slices_left: int = slice_start - slice_eaten
            if slice_start > slice_eaten:
                print("You have" ,slices_left, "slices of pizza left\n")
# the code below will make it so if the user inputs that they have eaten more pizza slices than they started with they will receive an error message and go back to the start
            elif slice_start < slice_eaten:
                print("You must have entered the wrong numbers try again\n")
        elif choice == 0:
            break
    except Exception:
        print("Please enter a number")
# all questions and the code for them need to be implemented along with error handling for all the inputs as completed above
# if the user inputs a number which is lower than or equal to 0 they will be sent back to the start of the programme with an error message

# bibliography
# Ghadge, D., 2023. Building a Command-Line Menu in Python: Exploring Different Applications. [Online]
# Available at: https://medium.com/@dghadge2002/building-a-command-line-menu-in-python-exploring-different-applications-f970a61e6412
# [Accessed 1 March 2024]
# w3schools, n.d. Python Try Except. [Online]
# Available at: https://www.w3schools.com/python/python_try_except.asp
# [Accessed 1 March 2024]