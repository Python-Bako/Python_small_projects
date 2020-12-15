import random

def random_walk2(n):
    """returns the coordinates after n random walks"""
    x,y = 0,0
    
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(-1,0),(1,0)])
        x += dx
        y += dy
    return (x,y)



# Use Monte Carlo technique for answering to the following question

"""
What is the longest walk you can take so on average you will end
up 4 blocks fewer from home
"""

number_of_walks = 10000

for walk_length in range(1,31):
    no_transport = 0 # number of walks or fewer blocks from home
    for i in range(number_of_walks):
        (x,y) = random_walk2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
        no_transport_percentage = float(no_transport) / number_of_walks

    print("Walk size ", walk_length, " / % of no transport = ",
          100 * no_transport_percentage)
        

    

    
