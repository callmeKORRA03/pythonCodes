# def fun_name(full_name, enter_year, current_year=2022):
#     year_cal = current_year - enter_year
#     full_details = 'Good Day Mr/Mrs {}, Your born in {} and your currently {} years old ' .format(
#         full_name, enter_year, year_cal)
#     return full_details


# print(fun_name(input('Enter Full name'), int(input('Enter Year Born'))))

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob'))
