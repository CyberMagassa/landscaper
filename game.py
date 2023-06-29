total_earnings = 0

while True:
    user_input = input('Do you want to cut a lawn? (yes/no): ')
    
    if user_input.lower() =='yes':
        total_earnings +=1
        print('You cut a lawn! Your total eanrnings: $', total_earnings)
    elif user_input.lower() == 'no':
        print('You decided to stop working. Your total earnings for the day: $', total_earnings)
        break
    else:
        print("Invalid input. Please enter a 'yes'or a 'no'")
