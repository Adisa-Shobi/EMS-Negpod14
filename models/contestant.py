#!/usr/bin/python3
"""
Defines contestant class which manages each contestant and their votes
"""

class Contestant:
    '''
    Represents a single contestant
    '''
    nb_contestants = 0
    def __init__(self, name="", origin="", description="", DOB="", password="", link=""):
        """
        Initializes a new Contestant object.
       :param name: The name of the contestant
       :param origin: The origin of the contestant
       :param Biography: The biography of the contestant
       :param DOB: The date of birth of the contestant
       """
        Contestant.nb_contestants += 1
        self.__id = Contestant.nb_contestants
        self.__name = name
        self.__origin = origin
        self.__description = description
        self.__password = password
        self.__link = link
        self.__DOB = DOB
        self.__vote_count = 0

    def add_vote(self):
        """
        Increments contestant vote by 1
        """
        self.__vote_count += 1

    @property
    def id(self):
        """
        Getter for contestants id
        """
        return self.__id

    @property
    def name(self):
        """
        Getter for contestants name
        """
        return self.__name

    @property
    def vote_count(self):
        '''
        Number of votes for contestant
        '''
        return self.__vote_count

        # A function print_summary that prints a summarized version of contestant information
    def print_summary(self):
        """
        Prints a summary of contestants information
        """
        # Define the border string
        LENGTH = len(self.__name) + 30
        border = " —" + "-" * (len(self.__name) + 28) + "— "

        #print the contestant summary

        print(border)
        line = f"Contestant: {self.__id:02d}"
        print("|" + line + (LENGTH - len(line)) * " " +"|")
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
