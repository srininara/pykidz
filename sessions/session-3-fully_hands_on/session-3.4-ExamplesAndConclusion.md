<slide>
Welcome back! In this part we are going to actually apply the concepts we learnt in the previous parts and create programs that do something and can be run again and again.

## Example 1 - A simple interest calculator

First let us create a simple interest calculator.

```python
# principal = int(input("Please let me know your principal in Rs: "))
principal = float(input("Please let me know your principal in Rs: "))
rate = float(input("Please give me the rate of interest you are getting in %: "))
time = int(input("Please let me know the number of years you are investing: "))

# Formula for simple interest
si = principal * rate * time /100
print("***********************************************************")
print(f"Your investment: {principal}")
print(f"The rate applied: {rate}%")
print(f"The investment period: {term} years")
print(f"Simple interest you get the end of the period: Rs. {si}")
print(f"Total amount at the end of investment period: Rs. {si + principal}")
print("***********************************************************")

```
[Code reference](code/si_calculator.py)

The above example illustrates how by taking the input from the user we are able to provide them with useful information. If we did not get the input of the principal or rate or time from the user then the program would define these values inside the code which is not very useful to the end user.

## Example 2 - A greeter 

Let us now do our silly greeter. This time we will import some modules and use them here.

```python
from random import randint
from datetime import datetime
fname = input("Please tell me your first name: ")
lname = input("Please tell me your last name: ") 
print("***********************************")
# want to repeat greeting at random.
print(f"Hi! {fname} {lname}\n" * randint(1,10))
print("This is python greeter here!")
print("***********************************")
print(f'''How are you today, {fname}? 
Hope {datetime.today().strftime('%A, %B %d')} is a good day for you! 
Bye!''')
```
[Code reference](code/greeter.py)

## Conclusion

<slide>

We have developed and *saved two programs* that *interact with the user*, *import modules* from the python standard library to do different kinds of tricks and even *added some comments* to the code. 

You have practically used all the concepts you learn in this session. You also used some of the things which we learnt in earlier session. This concludes this session and all its parts. I will come back with a next topic in python. Please use the comments to ask your questions. Thanks and see you soon.

## References
- [Documentation for randint function inside random module](https://docs.python.org/3/library/random.html#random.randint)
- [Documentation for today function inside datetime class within datetime module](https://docs.python.org/3/library/datetime.html#datetime.datetime.today)
- [Documentation for strftime function inside datetime class within datetime module](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)