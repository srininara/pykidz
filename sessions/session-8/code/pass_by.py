def doubler(input):
    print("Inside the function", input)
    input = input * 2
    print("Inside the function after doubling", input)

def doubler_again(input):
    print("Inside the function", input[0])
    input = [input[0] * 2]
    print("Inside the function after doubling", input[0])

x = [20]
print("Inside main before function call", x[0])
doubler_again(x)
print("Inside main after function call", x[0])

