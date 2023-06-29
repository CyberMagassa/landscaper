total_earnings = 0
earnings_rate = 1

while True:
    user_input = input("What would you like to do? Enter 'work' to cut a lawn, 'buy' to purchase scissors, or 'quit' to stop for the day: ")

    if user_input.lower() == "work":
        total_earnings += earnings_rate
        print("You cut a lawn! Your total earnings: $", total_earnings)
        print()  # Line break
    elif user_input.lower() == "buy":
        cost = 10  # Cost of purchasing scissors
        if total_earnings >= cost:
            total_earnings -= cost
            earnings_rate += 4
            print("You purchased scissors! Your earnings rate has increased.")
            print("Your current earnings rate: ", earnings_rate)
        else:
            print("Insufficient funds to purchase scissors.")
        print()  # Line break
    elif user_input.lower() == "quit":
        print("You decided to stop working. Your total earnings for the day: $", total_earnings)
        break
    else:
        print("Invalid input. Please enter 'work', 'buy', or 'quit'.")
        print()  # Line break


