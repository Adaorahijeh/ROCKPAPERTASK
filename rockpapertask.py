import random

def play():
    user = input("Pick a weapon: 'r' for Rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'IT\'s a tie'
    # r > s, s > p, p > r
    if win(user, computer):
        return 'WINNER!!'
    else:
        return 'LOSER!!'    

def win(player, opponent):
    if (player== 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent =='r'):
        return 'True'

print(play())
