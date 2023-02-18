# a = int(input("Enter a value"))
# cod_tion = "{} is not even and is lesser than 50" .format(a)
# if a > 0:
#     if a > 30 and a % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print(cod_tion)

enter_age = int(input("Enter your age: "))
cod = "Your {} years old and too young to drive" .format(enter_age)
cod2 = "Your {} years old  and old enough to drive" .format(enter_age)
if enter_age > 18:
    print(cod2)
elif enter_age < 18:
    print(cod)
else:
    print("Enter a valid age not Alphabets")
