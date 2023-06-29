total_earnings = 0
earnings_rate = 1
has_rusty_scissors = False
has_push_lawnmower = False

while True:
    print("Available Tools:")
    if has_rusty_scissors:
        print("- Iron Scissors")
    if has_push_lawnmower:
        print("- Rocket Push Lawnmower")
    if not has_rusty_scissors and not has_push_lawnmower:
        print("- No tools or magics")

    user_input = input("What would you like to do? Enter 'work' to cut a lawn, 'buy' to purchase items, or 'quit' to stop for the day: ")

    if user_input.lower() == "work":
        if has_rusty_scissors:
            earnings_rate = 5
        elif has_push_lawnmower:
            earnings_rate = 25
        elif has_push_lawnmower and has_rusty_scissors:
            earnings_rate = 30
        else: 
            earnings_rate = 1      

        total_earnings += earnings_rate
        print("You cut a lawn! Your total earnings: $", total_earnings)
        print()  # Line break
    elif user_input.lower() == "buy":
        purchase_input = input("What would you like to buy? Enter 'scissors' or 'lawnmower': ")

        # Buy Scissors
        if purchase_input.lower() == "scissors":
            if not has_rusty_scissors:
                cost = 5
                if total_earnings >= cost:
                    total_earnings -= cost
                    has_rusty_scissors = True
                    earnings_rate = 5
                    print("You purchased a pair of scissors! Your earnings rate has increased.")
                    print("Your current earnings rate: ", earnings_rate)
                else:
                    print("Insufficient funds to purchase scissors.")
            else:
                print("You already have a pair of scissors.")
        # Buy Lawnmower
        elif purchase_input.lower() == "lawnmower":
            if has_push_lawnmower:
                print("You already have an old-timey push lawnmower.")
            elif total_earnings >= 25:
                total_earnings -= 25
                has_push_lawnmower = True
                earnings_rate = 25
                print("You purchased an old-timey push lawnmower! Your earnings rate has increased.")
                print("Your current earnings rate: ", earnings_rate)
            else:
                print("Insufficient funds to purchase a lawnmower.")
        else:
            print("Invalid item to purchase.")
        print()  # Line break
    elif user_input.lower() == "quit":
        print("You decided to stop working. Your total earnings for the day: $", total_earnings)
        has_rusty_scissors = False
        has_push_lawnmower = False
        break
    else:
        print("Invalid input. Please enter 'work', 'buy', or 'quit'.")
        print()  # Line break
