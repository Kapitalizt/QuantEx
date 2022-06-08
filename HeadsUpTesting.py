from numpy.random import choice
import matplotlib.pyplot as plt

t_num = int(input("Enter the number of trials in each group: "))
g_num = int(input("Enter number of trial groups: "))


def flip(flips):
    r = [0,1]
    trials = 0
    for i in range(flips):
        trials += choice(r, p = [0.3,0.7], replace = True)
    return trials

def trial_count(t_num, g_num):
    histo_data = []

    while g_num > 0:
        histo_data.append(flip(t_num))
        g_num -= 1

    #print(histo_data)
    return histo_data

def histo(t_num,g_num):    
    histo = trial_count(t_num,g_num)
    #print(histo)

    range = (min(histo),max(histo))
    bins = max(histo) - min(histo) + 1

    ev = sum(histo)/len(histo)

    plt.hist(histo,bins,range,color='blue',histtype = 'bar', rwidth = 0.5)

    plt.xlabel(f'Sum of {t_num} Trials \n E(X) = {ev}')
    plt.ylabel('Number of Results')
    plt.title(f'Distribution of {g_num} Flip Trials')

    plt.show()

histo(t_num,g_num)
