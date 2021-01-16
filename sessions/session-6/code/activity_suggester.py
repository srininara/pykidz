weather_good = input("Is the weather good outside? (Answer Yes/No): ")
have_cycle = input("Do you have a cycle? (Answer Yes/No): ")
if weather_good.upper() == 'YES':
    if have_cycle.upper() == 'YES':
        print("Go out for a cycle ride!")
    else:
        print("Walk in the park...")
    print("Play cricket with your friends!")
elif weather_good.upper() == 'NO':
    print("Play a game of carrom or chess")
    print("Chat with family!")
    print("Take a nap....")
else:
    print("If you can't answer this question properly...")
    print("You should go back to bed!")
print("Ok bye!")
