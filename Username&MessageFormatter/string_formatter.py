# Username and message formatter

# collect variables

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()
bio = input("Tell us a litte about yourself: ")

#create username
username = f"{first[0].lower()}{last.lower()}"

# full name
full_name = f"{first.title()} {last.title()}"

#clean up bio
clean_bio = bio.strip()

# count characters
bio_length = len(clean_bio)

# replace text
updated_bio = clean_bio.replace("I am", "I'm")

# display output
print("/n========== USER PROFILE ==========")
print(f"Full Name: {full_name}")
print(f"Username: {username}")
print(f"Bio: {updated_bio}")
print(f"Bio Length: {bio_length} characters")