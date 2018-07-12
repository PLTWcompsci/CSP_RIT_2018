####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'ML**2' # Only 10 chars displayed.
strategy_name = 'Likelihoods'
strategy_description = '''
If opponent is extremely likely to be predictable, betray; otherwise, if they
frequently betrayed after my previous move, betray. Otherwise, collude.
'''

def likelihood_they_betray( their_history ):
    if len( their_history ) == 0:
        return 0

    betrayals = 0
    for each in their_history:
        if each == 'b':
            betrayals += 1

    return float(betrayals) / len( their_history )

def likelihood_they_betray_after( their_history, my_history, move ):
    if len( their_history ) == 0:
        return 0

    betrayals = 0
    occurences = 0
    for i in range(1, len(their_history)):
        if my_history[i-1] == move:
            occurences += 1
            if their_history[i] == 'b':
                betrayals += 1

    if occurences == 0:
        return 0

    return float(betrayals) / occurences

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.

    Make my move.
    Returns 'c' or 'b'.
    '''
    if len(my_history)==0:
        return 'c'
    betrayal_likelihood = likelihood_they_betray( their_history )
    # Just can't trust that ruddy bastard
    if betrayal_likelihood > .8:
        return 'b'
    # Oh, so naive ... how can you not take advantage?
    if betrayal_likelihood < .1:
        return 'b'
    # Barring extremes above, collude unless they are likely
    # to betray after my most recent move
    betrayal_after_my_move = likelihood_they_betray_after( their_history, my_history, my_history[-1] )
    # If they tend to betray after my previous move, betray
    if betrayal_after_my_move > .8:
        return 'b'
    return 'c'

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

#    return 'c'

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':

    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='',
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc',
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0,
              their_score=0,
              result='b')
