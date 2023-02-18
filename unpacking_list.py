# tuple_numbers = [1, 2, 3, 4, 5]
# first, *middle, last = lst
# print(first, *middle)

# Unpacking dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
# Asabeneh lives in Finland, Helsinki. He is 250 years old.
print(unpacking_person_info(**dct))
