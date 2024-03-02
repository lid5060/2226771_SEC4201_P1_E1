print("Welcome to the programme")
print("Enter a number between 1 - 9 to pick which question to go to or enter 0 to exit")
# try is being used to try and run the code if an integer is not used then an error will occur which we be dipslayed to the user and the programme will loop
# error handling is broken again fix it!!!! when implimented above and below choice = int it either says that it isn't refrenced or it just skips past the error
# error handling now seems to be working
while True:
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