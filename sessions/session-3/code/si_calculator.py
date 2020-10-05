principal = float(input("Please let me know your principal in Rs: "))
rate = float(input("Please give the rate of interest in %: "))
time = int(input("Please let me know the period of investment in years: "))

# This is the simple interest formula
si = principal * rate * time / 100
print("****************************************************")
print(f"Your invested principal: Rs. {principal}")
print(f"Your rate of interest obtained: {rate} %")
print(f"Your period of investment: {time} years")
print(f"Simple interest earned by you: Rs. {si}")
print(f"The amount earned at the end of investment period: Rs. {round(si + principal,2)}")
print("****************************************************")