import random

def random_walk(n):
    """return the x,y coordinates after n random walks"""

    x = 0
    y = 0

    for i in range(n):
        step = random.choice(["N","S","E","W"])

        if step == "N":
            x = x + 1
        elif step == "S":
            x = x - 1
        elif step == "E":
            y = y + 1
        else:
            y = y - 1

    return(x,y)
