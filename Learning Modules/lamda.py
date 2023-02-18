# def power(x):
#     return lambda n: x ** n


# # function power now need 2 arguments to run, in separate rounded brackets
# cube = power(2)(3)
# print(cube)          # 8

def sum_numbers(name):  # normal function
    return sum(name)


def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
