import random

def play():
    user = input("Your choice : 'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    comp = random.choice(['r','p','s'])

    if user==comp:
        return 'Tie'

    # r>s, s>p, p>r
    if win(user,comp):
        return 'WON!'
    
    return 'LOST!'

def win(player,opponent):
    # return true if player wins
    # r>s,s>p, p>r
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
    
print(play())