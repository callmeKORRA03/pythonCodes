def generate_name():
    first_name = input('Enter Full Name: ')
    age = int(input('Enter Your Age: '))
    language = input('What language are u learning: ')
    full_detail = 'Your name is {}, your {} years old And your currently learning {} to be a {} developer'.format(
        first_name, age, language, language)
    return full_detail


print(generate_name())
