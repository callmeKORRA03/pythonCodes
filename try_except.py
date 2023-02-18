# try:
#     print(10 + 7)
# except:
#     print('Something went wrong')

try:
    enter_name = input("Enter Full Name: ")
    enter_year_born = input("Enter Year Born: ")
    calculate_year = 2022 - enter_year_born
    print(
        f'Your name is {enter_name}, your born in the year  {enter_year_born}  and your currently {calculate_year} years old')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
