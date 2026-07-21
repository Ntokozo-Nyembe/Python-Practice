# Ask the user to enter their password
password = input("Enter your secret password: ").strip()

# get the first and last charaters
first_letter = password[0]
last_letter = password[-1]

# display the password hint
print(f"Password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}.")