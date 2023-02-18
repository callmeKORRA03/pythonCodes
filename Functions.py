# def generate_full_name():  # Simple Function
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name


# print(generate_full_name())  # Funtion with Parameters


# def is_even(n):
#     if n % 2 == 0:
#         # print('even')
#         return True
#     return False


# # inputing values to the parameters
# print(is_even(int(input("Input A Number: "))))

def calculate_age(birth_year, current_year=2022):
    age = current_year - birth_year
    return age


print('Your Age is:', calculate_age(
    int(input('Enter the year your were born:'))))

# def sum_all_nums(*nums):  # We Use this type of Function if we dont know the amount of parameters
#     total = 0
#     for num in nums:
#         total += num     # same as total = total + num
#     return total


# print(sum_all_nums(2, 3, 5))  # 10


# def sqaure_number(x):
#     return x*x


# def enter_number(enter_anynumber, square):
#     return enter_anynumber(square)


# print('The square of Your number is:', enter_number(
#     sqaure_number,   int(input('Enter any number'))))
