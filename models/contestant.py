#!/usr/bin/python3
"""
Defines contestant class which manages each contestant and their votes
"""

class Contestant:
    '''
    Represents a single contestant
    '''
    def __init__(self):
        self.__name = ""
        self.__origin = ""
        self.__Biography = ""
        self.__DOB = ""
    def set_contestant_info(self, name, origin, Biography, DOB):
        self.__name = name
        self.__origin = origin
        self.__Biography = Biography
        self.__DOB = DOB
# A function print_summary that prints a summarized version of contestant information
    def print_summary(self):
        # Define the border string
        border = " —" + "-" * (len(self.__name) + 18) + "— "

        #print the contestant summary
        
        print(border)
        print("|" + f"         {self.__name}" + "           |")
        print("|" + "                      " + "           |")
        print("|" + f" Name: {self.__name}" + "           |")


    # —----------------------------
    #|          Contestant 1      |
    #|     Name: Tinubu           |
    #|                            |
    #|                            |
    #|                            |
    # —----------------------------
