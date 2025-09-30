# 
import random

secret_guess = random.randint (1,7)
attempts = 0
max_attempts = 3

guess = int(input('Guess a number: '))

while guess != secret_guess and attempts < max_attempts-1:
    
    attempts +=1
    print('wrong guess, attempts left:', max_attempts-attempts)
    
    guess =int(input('Guess a number: '))
if guess == secret_guess:
    print('right guess')
else:
    print('you have exhauted all the attempts, log out')