person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# print(person.get('first_name'))  # Asabeneh
# print(person.get('country'))    # Finland
# # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
# print(person.get('skills'))
# print(person.get('city'))   # None
# print(person.get('age'))

person_index = person[2]
print(person_index)
