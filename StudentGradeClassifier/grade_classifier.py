# Student grade classifier

# Collect learner information
learner_name = input("Enter Learner's name: ")

subject1 =  float(input("Enter Subject 1 marks: "))
subject2 =  float(input("Enter Subject 2 marks: "))
subject3 =  float(input("Enter Subject 3 marks: "))

# calculaye the average
average = round((subject1 + subject2 + subject3) / 3, 2)

# pass or faiil
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# assign a letter grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else: 
    grade = "F"

# Display report card
print("\n============ STUDENT REPORT CARD =============")
print(f"Learner: {learner_name}")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Average: {average}")
print(f"Grade: {grade}")
print(f"Status: {status}")

# Check for intervention

print("\nIntervention Check:")

if subject1 < 40:
    print("* Subject 1 needs intervention.")

if subject2 < 40:
    print("* Subject 2 needs intervention.")

if subject3 < 40:
    print("* Subject 3 needs intervention.")

if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
    print("* No intervention required.")

print("================================================")