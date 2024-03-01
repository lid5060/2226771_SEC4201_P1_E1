while True:
    print("Welcome to the programme")
    print("Enter a number between 1 - 9 to pick which question to go to or enter 0 to exit")
# try is being used to try and run the code if an integer isnt used then an error will occur which we be dipslayed to the user and the programme will loop
    try:
        choice = int(input())
    except:
        print("Please enter a whole number")
    finally:
        if choice < 0:
            print("Hello")
        elif choice > 9:
            print("World")
        elif choice == 0:
            break
# if the user inputs a number which is lower than or equal to 0 they will be sent back to the start of the programme with an error message
# bibliography
#Ghadge, D., 2023. Building a Command-Line Menu in Python: Exploring Different Applications. [Online]
#Available at: https://medium.com/@dghadge2002/building-a-command-line-menu-in-python-exploring-different-applications-f970a61e6412
#[Accessed 1 March 2024]
#w3schools, n.d. Python Try Except. [Online]
#Available at: https://www.w3schools.com/python/python_try_except.asp
#[Accessed 1 March 2024]