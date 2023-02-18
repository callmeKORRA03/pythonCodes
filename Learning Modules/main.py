# import mymodule
# print(mymodule.enter_name(input('Enter Your First Name:'),
#       input('Enter Second Name:')))

# import string
# print(string.ascii_uppercase)

from random import randint
guess_number = randint(5, 6)
enter_number = int(input("Guess a number: "))
guess_number = randint(5, 20)
print(guess_number)
if enter_number == guess_number:
    print('Guess was Right')
else:
    print('Try again')
