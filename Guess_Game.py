from random import randint
random_number = randint(1, 20)
print(random_number)
guess_number = int(input('Guess a number from 1 - 20: '))
if guess_number == random_number:
    print('Congrats, Guess is Correct')
else:
    print('Please Try Again')
