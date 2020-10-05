from random import randint
from datetime import datetime

fname = input("Please tell me your first name: ")
lname = input("Please tell me your last name: ")
print(f"Hi! {fname} {lname} \n" * randint(1,10))
print("This is python greeter here!")
print(f'''How are you today, {fname}
Hope {datetime.today().strftime('%A, %B %d')} is a good day for you!
Bye!''')