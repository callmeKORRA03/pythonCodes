class Person:
    def __init__(self, firstname, lastname, age, country,) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country

    def person_info(self):
        return f'Your name is {self.lastname} {self.firstname}, your {self.age} years old and he live in {self.country}'


g = Person(input('Enter First Name: '), input('Enter Last Name: '),
           input('Enter your Age: '), input('Where are you from: '))
print(g.person_info())
