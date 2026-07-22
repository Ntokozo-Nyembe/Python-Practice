# multi functional calculator

# collect numbers from user
num1 = float(input("Enter your number: "))
num2 = float(input("Enter your second number: "))

# perform calculations + - *
add = round(num1 + num2, 2)
subtract = round(num1 - num2, 2)
multiply = round(num1 * num2, 2)

print("\n============CALCULATOR RESULTS============")
print(f"Addition:        {add}")
print(f"Substraction:    {subtract}")
print(f"Multiplication:  {multiply}")

# Dividion and modulus calculations
if num2 == 0:
    print("Division:         Cannot divide by zero.")
    print("Floor Division:   Cannot divide by zero.")
    print("Modulus:          Cannot divide by zero.")
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"Division:         {division}")
    print(f"Floor Division:   {floor_division}")
    print(f"Modulus:          {modulus}")

print("===================================================")
