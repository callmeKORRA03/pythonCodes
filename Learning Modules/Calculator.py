first_number = int(input("Enter Your first Number: "))
second_number = int(input("Enter Your second Number: "))
operand = input("Enter an operand + - / *: ")

if operand == '+':
    print("The result of this using " + operand + " is = ",
          first_number + second_number)
elif operand == '-':
    print("The result of this using " + operand + " is = ",
          first_number - second_number)
elif operand == '/':
    print("The result of this using " + operand + " is = ",
          first_number / second_number)
elif operand == '*':
    print("The result of this using " + operand + " is = ",
          first_number * second_number)
elif operand == '**':
    print("The result of this using " + operand + " is = ",
          first_number ** second_number)

else:
    print("invalid operand")
