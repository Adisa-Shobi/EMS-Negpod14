#!/usr/bin/python3
"""
Program entry point
"""
from mailbox import Message
import os
import time
from datetime import datetime
from models.contestant import Contestant
from models.votes import Vote
from models.session import Session
from utils import welcome_message
import utils
import time
import os


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
            Press '4' to quit.\nPlease select a choice: ")
        if choice == "1":
            view_contestants(10)
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
        time.sleep(3)
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
    try:
        duration = int(duration)
    except Exception as e:
        print("Duration must be in an interger")
        return
    if duration < 1 or duration > 20:
        print("Duration must be greater than 0 and less than 20")
        return
    COUNTDOWN = 5
    while COUNTDOWN > 0:
        os.system('clear')
        print(f"Session starts in {COUNTDOWN}")
        time.sleep(1)
        COUNTDOWN -= 1
    session = init_session(duration)
    session.print_summary(contestants)
    input("Press any key to exit: ")

def init_session(duration):
    # TODO: @Jules you can implement this part

#Kuir's task: veiwing contestansts function
def view_contestants(sleep_time):
    if not is_contestants():
        return
    else:
        for contestant in contestants:
            contestant.print_summary()
    time.sleep(sleep_time)

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
    time.sleep(2)

if __name__ == "__main__":
    main()
