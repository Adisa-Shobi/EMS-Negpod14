"""
Defines class that serves as session manager
"""
import time
import utils
import os

class Session:
    '''
    Properties:
    @duration: The amount of time the session will last for
    '''
    def __init__(self, duration, start_time):
        '''
        Init function
        '''
        self.duration = duration
        self.start_time = start_time
        self.__votes = []

    def add_vote(self, vote):
        '''
        Adds vote to list of votes in session
        '''
        self.__votes.append(vote)

    @property
    def votes(self):
        '''
        Getter for votes 
        '''
        return self.__votes

    def print_summary(self, contestants):
        '''
        Prints a summary of the election results
        '''
        os.system('clear')
        result_dict = {key.name: key.vote_count for key in contestants}
        utils.print_bar_chart(result_dict)
        print(utils.winner)
        winner = max(contestants, key=lambda x: x.vote_count)
        print(f"\033[1;31;40m{winner.name}\033[0m")
        headers = ['Name', 'Votes']
        data = [[item.name, item.vote_count] for item in contestants]
        utils.print_table(data, headers)
        time.sleep(5)
