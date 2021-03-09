import random

# User can pick 6 numbers

def getPlayer_numbers():
    number_csv = input("Enter your 6 numbers, seperated by commas: ")
    # Now, I want to create a set of integers for this number_csv
    number_list = number_csv.split(",") # ["3","44","2","33"] smt like that
    # Create now a set of integers
    integer_set = {int(number) for number in number_list}
    return(integer_set)


# Lottery calculates 6 random numbers (between 1 and 20)
def createLottery_numbers():
    values = set() # CANNOT initialize like so: {}
    # for i in range(6): # the problem with that loop is that can return more than once the same value, so the set will not have 6 values at the end
    while len(values) < 6: # this way we can assure that the loop will be running till we get 6 values in our set
        values.add(random.randint(1,20))
    return(values)



# Then we match the lottery numbers to the user numbers

def menu():
    # Ask players for numbers
    player_numbers = getPlayer_numbers()

    # Calculate lottery numbers
    lottery_numbers = createLottery_numbers()

    # Print out the winnings
    winnings = player_numbers.intersection(lottery_numbers)
    print(f"You won {len(winnings)*10000} dollars. \n Your winning numbers were the following: {winnings}")
# Calculate the winnings based on how many numbers we matched

menu()