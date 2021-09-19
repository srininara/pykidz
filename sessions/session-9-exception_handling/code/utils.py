def divide(dividend, divisor):
    # Validating if we are getting numbers only in the input.
    if not dividend.isnumeric() or not divisor.isnumeric():
        # if either of them are not numeric then we throw or raise the
        # corresponding built-in exception in Python
        raise TypeError(f"Only numeric values are supported as input. {dividend} or {divisor} is not numeric.")
    dd = int(dividend)
    dr = int(divisor)
    if dr == 0:
        raise ValueError("divisor cannot be 0")
    return dd/dr
