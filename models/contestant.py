#!/usr/bin/python3
"""
Defines contestant class which manages each contestant and their votes
"""

class Contestant:
    '''
    Represents a single contestant
    '''
     def __init__(self, name="", origin="", Biography="", DOB=""):
     """
       Initializes a new Contestant object.

       :param name: The name of the contestant
       :param origin: The origin of the contestant
       :param Biography: The biography of the contestant
       :param DOB: The date of birth of the contestant
       """
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
        print("|" + f"  {self.__name}" + "           |")
        print("|" + "                " + "           |")
        print("|" + f" Name: {self.__name}" + "      |")
        print("|" + f" Origin: {self.__origin}" + "  |")
        print("|" + f" Bio: {self.__Biography}" + "  |")
        print("|" + f" DOB: {self.__DOB}" + "        |")
        print(border)
