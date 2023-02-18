# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable


def is_name_long(name):
    if len(name) > 7:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
