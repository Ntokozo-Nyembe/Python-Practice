# calculating a tip 

bill = float(input("Enter the bill: R"))
tip = 0.15 # written in decimal

value_tip = bill * tip
total_cost = bill + value_tip

print(f"Here is the tip: {value_tip}")
print(f"Here is the tip: {round(value_tip, 2)} rounded")

print(f"Here is the total cost: {total_cost}")
print(f"Here is the total cost: {round(total_cost, 2)} Rounded")