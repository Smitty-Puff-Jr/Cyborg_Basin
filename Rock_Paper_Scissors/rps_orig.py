from random import randint
import random

choice = ['Rock', 'Paper', 'Scissor']
user_choice = input('(R)ock, (P)aper, or (S)cissors? ')
#value = randint(0, len(choice)-1)
opponent_choice = random.choice(choice)
print(opponent_choice)
#print(len(choice))
if user_choice.upper() == 'R' and opponent_choice == 'Rock':
    outcome = 'tie'
if user_choice.upper() == 'R' and opponent_choice == 'Paper':
    outcome = 'l'
if user_choice.upper() == 'R' and opponent_choice == 'Scissor':
    outcome = 'w'

if user_choice.upper() == 'S' and opponent_choice == 'Rock':
    outcome = 'l'
if user_choice.upper() == 'S' and opponent_choice == 'Paper':
    outcome = 'w'
if user_choice.upper() == 'S' and opponent_choice == 'Scissor':
    outcome = 'tie'

if user_choice.upper() == 'P' and opponent_choice == 'Rock':
    outcome = 'w'
if user_choice.upper() == 'P' and opponent_choice == 'Paper':
    outcome = 'tie'
if user_choice.upper() == 'P' and opponent_choice == 'Scissor':
    outcome = 'l'

print(outcome)
#print(opponent_choice)
