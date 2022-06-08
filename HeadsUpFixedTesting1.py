import matplotlib.pyplot as plt
import random

def pop_list(cust_count):
    cust_list = []
    cust_num = 1

    while cust_count > 0:
        cust_list.append(cust_num)
        cust_num += 1
        cust_count -= 1

    return cust_list
        

def exp_selection(t_num):

    if t_num <= 0:
        while True:
            try:
                cust_count = int(input("Please enter the number of potential customers: "))
                if cust_count <= 0:
                    print("Please enter a non-zero positive integer.")
                    continue   
                break
            except:
                print("Please enter a non-zero positive integer.")
                continue
    else:
        cust_count = t_num

    cust_list = pop_list(cust_count)
    exp_count = int(cust_count/2)
        
    exp_list = random.sample(cust_list,exp_count)
    exp_list = sorted(exp_list)

    exp_count = int(len(exp_list))
    
    return exp_count
    #print(f"""\n    ***********************
    #Of [{cust_count}] potential customers, [{exp_count}] were selected for management's experiment. 
    #The customers in the potential pool have been given ascending ID numbers and selected at random.
    # 
    #The following customers are to be included in the experiment:
    #{exp_list}
    #\n    ***********************
    #""")

def trial_count(t_num, g_num):
    histo_data = []

    while g_num > 0:
        histo_data.append(exp_selection(t_num))
        g_num -= 1

    #print(histo_data)
    return histo_data

def histo():  
    t_num = int(input("Enter the number of trials in each group: "))
    g_num = int(input("Enter number of trial groups: "))
  
    histo = trial_count(t_num, g_num)
    #print(histo)
    

    range = (min(histo)-3,max(histo)+3)
    bins = max(histo) - min(histo) + 7

    ev = sum(histo)/len(histo)

    plt.hist(histo,bins,range,color='blue',histtype = 'bar', rwidth = 0.5)

    plt.xlabel(f'Sum of {t_num} Trials \n E(X) = {ev}')
    plt.ylabel('Number of Results')
    plt.title(f'Distribution of {g_num} Flip Trials')

    plt.show()

histo()
