#!/usr/bin/python3
"""
Program entry point
"""
from mailbox import Message
import os
import time
from models.contestant import Contestant
from constants import welcome_message


# TODO: @Kuir Define a function view_contestants that handle when the user picks option 1
# TODO: @Mugisha Define a function register_contestant to handle when the user picks option 2
# TODO: @Shobi Define a function start_session that handles when the user picks option 3

contestants = []
def main():
    '''
    Starts program flow
    '''
    # TODO: @Eddy write code to print the options the user can chose from on start of the applicaion
    # Please pick an option
    # 1). View contestants   2). Register contestant   3). Start voting session
    running = True
    while running:
        os.system('clear')
        print(welcome_message)
        print("Press the following numbers that corresponds to with your choice.")
        choice = input(
            "\
            Press '1' to view contestants \n\
            Press '2' to register contestants \n\
            Press '3' to start a session\n\
            Press '4' to quit.\n")
        if choice == "1":
            view_contestants()
        elif choice == "2":
            register_contestant()
        elif choice == "3":
            start_session()
        elif choice == "4":
            print("Program succesfully closed")
            running = False
        else :
            print(choice)
            print("Wrong input. Try again!")
            pass

        pass

def is_contestants():
    '''
    Checks if contestants have been registered
    '''
    if len(contestants) == 0:
        print("No contestants added")
        print("Please register contestant to continue")
        time.sleep(1)
        return False
    return True

def start_session():
    '''
    Starts voting session based on currently added contestants
    '''
    os.system('clear')
    if not is_contestants():
        return
    duration = input("Please enter voting session duration(mins): ")
    COUNTDOWN = 5
    while COUNTDOWN > 0:
        os.system('clear')
        print(f"Session starts in {COUNTDOWN}")
        time.sleep(1)
        COUNTDOWN -= 1
    init_session()

def init_session():
    '''
    App flow for voting session
    '''
    # TODO: @Jules you can implement this part

#Kuir's task: veiwing contestansts function
def view_contestants():
    if len(contestants) == 0:
        print("No contestants added")
        time.sleep(1)
    else:
        for contestant in contestants:
            contestant.print_summary()
    time.sleep(1000)

#Mugisha's task: Register contestant function
# Function to register a contestant
def register_contestant():
    print("\nEnter contestant details:")
    name = input("Name: ")
    origin = input("Place of origin: ")
    dob = input("D.O.B: ")
    link = input("Bio link (optional): ")
    description = input("Write a short description: ")
    password = input("Please enter a password: ")

    contestant = Contestant(name=name, origin=origin, DOB=dob, password=password, link=link)

    contestants.append(contestant)
    print("Contestant registered!")

if __name__ == "__main__":
    main()
