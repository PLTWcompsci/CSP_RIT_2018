import matplotlib as plt
import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


team_name = 'Average' # Only 10 chars displayed.
strategy_name = 'The Law of Averages Strategy'
strategy_description = 'If the preponderance of their moves indicate that they collude more than betray, the move would be to betray. If the preponderance of their moves is to betray, the move would be to betray. Otherwise, the move is random.'

    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(their_history)-their_history.count('b')==len(their_history):
        return random.choice(['b','c'])
    else:
        return 'b'
        
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    