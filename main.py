#!/usr/bin/python3
"""
Program entry point
"""

# TODO: @Kuir Define a function view_contestants that handle when the user picks option 1
# TODO: @Mugisha Define a function register_contestant to handle when the user picks option 2
# TODO: @Shobi Define a function start_session that handles when the user picks option 3

def main():
    '''
    Starts program flow
    '''
    # TODO: @Eddy write code to print the options the user can chose from on start of the applicaion
    # Please pick an option
    # 1). View contestants   2). Register contestant   3). Start voting session

    pass

if __name__ == "__main__":
    main()

#Mugisha's task: Register contestant function
# Function to register a contestant
def register_contestant():
    print("\nEnter contestant details:")
    name = input("Name: ")
    origin = input("Place of origin: ")
    dob = input("D.O.B: ")
    link = input("Bio link (optional): ")
    description = input("Write a short description: ")

    contestant = {
        "name": name,
        "origin": origin,
        "dob": dob,
        "link": link,
        "description": description
    }

    contestants.append(contestant)
    print("Contestant registered!")
