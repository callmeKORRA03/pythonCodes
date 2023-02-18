first_name = input('Enter First Name: ')
second_name = input('Enter Second Name: ')
language = input('Enter Language you want to learn: ')
if 'F' in first_name and 'C' in second_name:
    print("WELCOME")
else:
    print("F and C must be in urname to be able to login")

full_name = 'Your first name is {} and your last name is {} and u want to learn {}' .format(
    first_name, second_name, language)

print(full_name)
