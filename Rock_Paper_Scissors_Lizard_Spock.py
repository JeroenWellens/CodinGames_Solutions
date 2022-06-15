import sys
import math

'''
Input
Line 1: an integer N representing the number of participants in the competition
Lines 2 to N+1: an integer NUMPLAYER indicating the player number (players have distinct numbers between 1 and N) followed by a letter 'R', 'P', 'C', 'L' or 'S' indicating the chosen sign SIGNPLAYER
Output
Line 1: the number of the winner
Line 2: the list of its opponents separated by spaces
'''
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
players = []
contestants = {}
with open('source.txt') as f:

    n = int(f.readline())
    for i in range(n):
        inputs = f.readline().split()
        numplayer = int(inputs[0])
        signplayer = inputs[1]
        players.append(numplayer)
        wins = []
        contestants.update({numplayer:(signplayer,wins)}) #number, sign, won against
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def determine_winner(player1,player2,contestants=contestants):
    '''
    Determine the winner between 2 players.
    
    Each player chooses a sign that he will keep throughout the tournament among:
    Rock (R)
    Paper (P)
    sCissors (C)
    Lizard (L)
    Spock (S)
    
    C > P or L; 
    P > R or S; 
    R > L or C; 
    L > S or P; 
    S > C or R 
    
    Return (number_winner,number_loser)
    
    update to code: changed from playerx being tupple to being a single number with a dictionary of contestants
    '''
    num1=player1
    sign1=contestants[num1][0]
    num2=player2
    sign2=contestants[num2][0]
    
    # If both players have the same sign, the lower player_number is the winner
    if sign1==sign2:
        if num1<num2:
            outcome = (num1,num2)
        else:
            outcome = (num2,num1)
    
    #Check if player1 wins the bout
    elif sign1 == 'C' and sign2 in 'PL':
        outcome = (num1,num2)
    elif sign1 == 'P' and sign2 in 'RS':
        outcome = (num1,num2)
    elif sign1 == 'R' and sign2 in 'LC':
        outcome = (num1,num2)
    elif sign1 == 'L' and sign2 in 'SP':
        outcome = (num1,num2)
    elif sign1 == 'S' and sign2 in 'CR':
        outcome = (num1,num2)

    #If there is no tie and player1 doesn't win, player 2 wins
    else:
        outcome = (num2,num1)
    # print(f'player {num1}: {sign1},player {num2}:{sign2}, bout is won by {outcome[0]}')
    return outcome

def play_round(players):
    winners = []
    for match in range(len(players)//2):
        win,lose = determine_winner(players[2*match],players[2*match+1])
        winners.append(win)
        contestants[win][1].append(lose)
    return winners 

while len(players)>1:
    # print(players)
    # print(contestants)
    players = play_round(players)

'''Give the desired output
Output
Line 1: the number of the winner
Line 2: the list of its opponents separated by spaces
'''
print(players[0])
streak = " ".join(map(str,contestants[players[0]][1]))
print(streak)