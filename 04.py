#%% Password rules
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; 
# they only ever increase or stay the same (like 111123 or 135679)

#%%
def check_six_digits(num):
    if num//100000>0 and num//100000<10:
        return True
    else:
        return False
        
#%%
def check_same_adj(num):
    strf=str(num)
    for a,b in zip(strf,strf[1:]):
        if a==b:
            return True
    return False

#%%
def check_decrease(num):
    strf=str(num)
    current=0
    for i in strf:
        cursor=int(i)
        if cursor<current:
            return False
        else:
            current=cursor
    return True

#%%
def run_tests(str_range):
    start,end=str_range.split('-')
    start,end=int(start),int(end)
    
    pass_counter=0
    for i in range(start,end):
        if check_six_digits(i):
            if check_same_adj(i):
                if check_decrease(i):
                    pass_counter+=1
    
    return pass_counter


#%% Puzzle input
puzzle_input='234208-765869'

# %% Part A
run_tests(puzzle_input)


# %%
def check_same_adj_b(num):
    strf=str(num)
    pairs=[]
    for a,b in zip(strf,strf[1:]):
        if a==b:
            pairs.append((a,b))
    eligible = [x for x in pairs if pairs.count(x) == 1]
    if len(eligible)>0:
        return True
    return False

# %% Tests
assert check_same_adj_b(112233)==True
assert check_same_adj_b(123444)==False
assert check_same_adj_b(111122)==True

# %%
def run_tests_b(str_range):
    start,end=str_range.split('-')
    start,end=int(start),int(end)
    
    pass_counter=0
    for i in range(start,end):
        if check_six_digits(i):
            if check_same_adj_b(i):
                if check_decrease(i):
                    pass_counter+=1
    
    return pass_counter

# %% Part B
run_tests_b(puzzle_input)


# %%
