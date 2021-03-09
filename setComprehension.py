# Sets in python are quite similar to lists, with the difference
# that are a little bit smarter. For example a list is just storing
# a collection of items, even duplicates. Sets on the other hand remove duplicates

listA = [22,22,3,4,5,66,22]
print(listA)

setA = set()
setA.add(3)
print(setA)

# let's add another 3
setA.add(3)
print(setA) # it prints only once the duplicated element

# Create now two new sets
user_values = {11, 45, 77, 88} # this is another way of creating a set -> with {}

lottery_values = {11,88,66,31}

# finding the intersected values of the two sets
intersected_values = lottery_values.intersection(user_values)
print(intersected_values)