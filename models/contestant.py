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

    # TODO: @Mahamat define a function print_summary that prints a summarized version of contestant information
    # —----------------------------
    #|          Contestant 1      |
    #|     Name: Tinubu           |
    #|                            |
    #|                            |
    #|                            |
    # —----------------------------
