import utils as u
print("Welcome to the calculator! I can do number divisions for you")
print("------------------------------------------------------------")
while(True):
    print("Let me have the numbers please.")
    dividend = input("Dividend please: ")
    divisor = input("Divisor please: ")
    try:
        quotient = u.divide(dividend, divisor)
        print("The quotient value is ", quotient)
        print("-----------------------------------------------")
    except ValueError as error: # This is much better
        print("Skipping this division since the values provided are not divisible. Details:", error)
    except TypeError as type_err:
        print("Skipping this division since you are not passing numerals. Details:", type_err)
    do_more = input("Do you want to do more? If so say y: ")
    print("-----------------------------------------------")
    if do_more !="y":
        break
print("Good bye!")