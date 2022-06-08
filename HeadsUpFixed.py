import random


def pop_list(cust_count):
    cust_list = []
    cust_num = 1

    while cust_count > 0:
        cust_list.append(cust_num)
        cust_num += 1
        cust_count -= 1

    return cust_list
        

def exp_selection():
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

    cust_list = pop_list(cust_count)
    exp_count = int(cust_count/2)
        
    exp_list = random.sample(cust_list,exp_count)
    exp_list = sorted(exp_list)

    exp_count = len(exp_list)
    
    print(f"""\n    ***********************
    Of [{cust_count}] potential customers, [{exp_count}] were selected for management's experiment. 
    The customers in the potential pool have been given ascending ID numbers and selected at random.
    
    The following customers are to be included in the experiment:
    {exp_list}
    \n    ***********************
    """)

exp_selection()