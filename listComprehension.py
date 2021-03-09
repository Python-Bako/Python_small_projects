##### List Comprehension ######
user_Input = "1,10,45,44,4"  
print(user_Input)

# split the list of strings into an array
user_Input = user_Input.split(",")
print(user_Input)

# append the string inputs into an array of numbers
user_input_asInt = [] # create an empty array

# append the elements of the list user_Input into an array, as numbers
for i in user_Input:
    user_input_asInt.append(int(i))

print(user_input_asInt)

#### Now, do the same as above with LIST COMPREHEMSION

# [number for number in user_Input] does the same as the for loop above
print([number for number in user_Input])

print([number*2 for number in user_Input])

# so now, with list comprehension we convert the elements above to integers as follows:
toInt = [int(N) for N in user_Input]
print(toInt)