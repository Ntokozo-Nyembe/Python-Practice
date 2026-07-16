# collet personal information from the user
name = input("Enter your First Name: ")
surname = input("Enter your Surname: ")
age = int(input("Enter you Age: "))
favourite_number = float(input("Enter your Favourite Number: "))

full_name = name + " " + surname
age_months = age * 12
rounded_number = round(favourite_number, 2)

#display formatted greeting using a f-string
print(f"Welcome , {full_name}!")

# display the name in UPPERCASE
print(full_name.upper())

# display the name in title case
print(full_name.title())

#display age in months
print(age_months)

#displying in a formatted profile card
print("\n=========== STUDENT PROFILE ==============")
print(f"Name: {full_name.title()}")
print(f"Age: {age} years")
print(f"Age in Months: {age_months}")
print(f"Favourite Number: {rounded_number:.2f}")
print("============================================")

print("\nData Types:")
print(type(name))
print(type(surname))
print(type(age))
print(type(favourite_number))

