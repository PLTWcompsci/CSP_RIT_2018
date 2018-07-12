team_name = 'Frank Lee Morris'
strategy_name = 'Mostly C til B'
strategy_description = 'Collude for 8 turns, then collude until betrayed'

def move(my_history, their_history, my_score, their_score):
    if len(their_history) <= 8:
        return 'c'
    else:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'