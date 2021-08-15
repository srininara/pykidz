def factor(dividend, divisor):
    print(f"finding if {divisor} is a factor of {dividend}")
    remainder = dividend % divisor
    return dividend % divisor == 0

val = factor(10,20)
if val:
    print("10 is a factor of 20")
else:
    print("10 is NOT a factor of 20")
