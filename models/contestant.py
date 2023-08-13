#!/usr/bin/python3
"""
Defines contestant class which manages each contestant and their votes
"""

class Contestant:
    '''
    Represents a single contestant
    '''
    def __init__(self, name="", origin="", description="", DOB="", password="", link=""):
        """
        Initializes a new Contestant object.
       :param name: The name of the contestant
       :param origin: The origin of the contestant
       :param Biography: The biography of the contestant
       :param DOB: The date of birth of the contestant
       """
        self.__name = name
        self.__origin = origin
        self.__description = description
        self.__password = password
        self.__link = link
        self.__DOB = DOB

        # A function print_summary that prints a summarized version of contestant information
    def print_summary(self):
        # Define the border string
        LENGTH = len(self.__name) + 30
        border = " —" + "-" * (len(self.__name) + 28) + "— "

        #print the contestant summary
        
        print(border)
        print("|" + self.__name + (LENGTH - len(self.__name)) * " " +"|")
        print("|"  + LENGTH * " " + "|")
        line = f" Name: {self.__name}"
        print("|" + line + (LENGTH - len(line)) * " " +"|")
        line = f" Origin: {self.__origin}"
        print("|" + line + (LENGTH - len(line)) * " " +"|")
        line = f" Desription: {self.__description}"
        print("|" + line + (LENGTH - len(line)) * " " +"|")
        line = f" Link: {self.__link}"
        print("|" + line + (LENGTH - len(line)) * " " +"|")
        line = f" DOB: {self.__DOB}"
        print("|" + line + (LENGTH - len(line)) * " " +"|")
        print(border)
