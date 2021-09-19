name = input("Please give me your name: ")
age = int(input("Please give me your age: "))
spl_adj = ""
if age < 0:
    spl_adj = "Mr Unborn"
elif age > 12 and age < 20:
    spl_adj = "Super Teen"
elif age > 19 and age < 30:
    spl_adj = "Vibrant Youth"
elif age >=0 and age <= 12:
    spl_adj = "Whizzo Kiddo"
else:
    spl_adj = "Oldie Moldie"
greeting = f"Hi {spl_adj}! {name}, you {age} year old!"
print(greeting)