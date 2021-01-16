principal = int(input("Please provide the amount in Rs you want to invest: "))
years = int(input("Please provide the number of years to invest: "))
inv1, inv2 = {}, {}
inv1["name"] = str(input("Please provide investment option 1 name: "))
inv1["rate"] = int(input("Investment option 1 interest rate: "))
inv1["type"] = str(input("Investment option 1 interest type (SI/CI): "))

inv2["name"] = str(input("Please provide investment option 2 name: "))
inv2["rate"] = int(input("Investment option 2 interest rate: "))
inv2["type"] = str(input("Investment option 2 interest type (SI/CI): "))
print("================================================================\n")

if inv1["type"].upper() == "SI":
    interest1 = round((principal * inv1["rate"] * years)/100, 2)
    print(f"Interest earned from {inv1['name']}: Rs. {interest1}")
elif inv1["type"].upper() == "CI":
    interest1 = round((principal * (1 + (inv1["rate"]/100))**years) - principal)
    print(f"Interest earned from {inv1['name']}: Rs. {interest1}")
else:
    interest1 = -1

if inv2["type"].upper() == "SI":
    interest2 = round((principal * inv2["rate"] * years)/100)
    print(f"Interest earned from {inv2['name']}: Rs. {interest2}")
elif inv2["type"].upper() == "CI":
    interest2 = round((principal * (1 + (inv2["rate"]/100))**years) - principal)
    print(f"Interest earned from {inv2['name']}: Rs. {interest2}")
else:
    interest2 = -1

if interest1 < 0 or interest2 < 0:
    print("Sorry, looks like you have provided wrong options. So not able to do any comparison!")
elif interest1 > interest2:
    print(f"Investing {inv1['name']} is better than {inv2['name']} by Rs {interest1 - interest2}")
elif interest2 > interest1:
    print(f"Investing in {inv2['name']} is better than {inv1['name']} by Rs {interest2 - interest1}")
else:
    print(f"Both options are good. You can pick either!")
   
print("Thanks!")