class Age:
    def __init__(self, numbers) -> None:
        self.numbers = numbers
        numbers = 31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26

    def age_numbers(self):
        return '{self.numbers}'


g = Age()
print(g.age_numbers())
