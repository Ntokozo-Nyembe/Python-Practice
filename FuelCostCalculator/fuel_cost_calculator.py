# South African Fuel Cost Calculator

# get user input
km = float(input("Enter the number of kilometers you want to drive: "))
petrol_price = float(input("Enter the current petrol price per liter (R): "))

#calculate fuel needed
liters_needed = km / 10

# total cost
total = round(liters_needed * petrol_price, 2)

# Display the results
print("\n========== FUEL COAT ESTIMATE ===========")
print(f"Distance:  {km} km")
print(f"Petrol Price: R{petrol_price: .2f} per liter")
print(f"Fuel Needed: {liters_needed: .2f} liters")
print(f"Estimated Fuel Cost: R{total: .2f}")
print("==============================================")


