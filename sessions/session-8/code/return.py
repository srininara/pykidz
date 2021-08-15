def age_commenter(age):
    if age < 0:
        print("Mr Unborn")
        return
    if age <= 12:
        print("Whizzo Kiddo")
        return
    if age < 20:
        print("Super Teen")
        return
    if age < 30:
        print("Vibrant Youth")
        return
    print("Oldie Moldie")


def simple_interest(principal, rate, term):
    if !type(principal) == int or !type(principal) == float:
        print("Error: Principal has to be a number")
        return
    if !type(rate) == int or !type(rate) == float:
        print("Error: Rate has to be a number")
        return
    # Do

age_commenter(28)
age_commenter(32)
age_commenter(6)  