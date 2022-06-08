from numpy.random import choice
def flip(flips):
    r = [0,1]
    trials = 0
    for i in range(flips):
        trials += choice(r, p = [0.3,0.7], replace = True)
    return trials
print(flip(100))