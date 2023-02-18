# a tuple is iniatlised with round brackets
tpl = ('Pea', 'Carrot', 'Grape', 'Apple', 'Bananna')
# input is used to accecpt string input from the user
enter_value = input('Guess a fruit')
if enter_value in tpl:
    print('Your guess is a correct guess')
else:
    print('Guess Wrong')
