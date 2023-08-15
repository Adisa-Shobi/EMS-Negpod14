"""
Class definition for vote handling. Each vote will be an instance of this
 class holding all necessary voting information
"""

class Vote:
    '''
    Properties:
    @name: Name of voter
    @age: Age of voter
    @voter_for: Id of contestant voted for
    '''
    def __init__(self, name='', age=0, voted_for=None, voters_id=None):
        self.name = name
        self.age = age
        self.voted_for = voted_for

