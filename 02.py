#%%
import pandas as pd
import numpy as np

#%%
with open('data/02.dat') as f:
    data=f.read()
    data=data.split(',')
    data=list(map(int,data))

#%%
def process(input_):
    """
    Input: List of integers
    Output: List of integers
    """
    output_=input_.copy()
    cursor=0
    while cursor < len(input_):
        opcode=output_[cursor]
        if opcode==99:
            break
        op1=output_[cursor+1]
        op2=output_[cursor+2]
        dest=output_[cursor+3]        
        if opcode==1:
            output_[dest]=output_[op1]+output_[op2]
            cursor+=4
        elif opcode==2:
            output_[dest]=output_[op1]*output_[op2]
            cursor+=4
        else:
            print(f'Error: {cursor}')
            break
    
    return output_
    

#%% Test
test_input=[1,9,10,3,2,3,11,0,99,30,40,50]
assert process(test_input)==[3500,9,10,70,2,3,11,0,99,30,40,50]

#%% More Tests
assert process([1,0,0,0,99])==[2,0,0,0,99]
assert process([2,3,0,3,99])==[2,3,0,6,99]
assert process([2,4,4,5,99,0])==[2,4,4,5,99,9801]

#%% Problematic test
assert process([1,1,1,4,99,5,6,0,99])==[30,1,1,4,2,5,6,0,99]

# %%
# Part A
# before running the program, 
# replace position 1 with the value 12 
# and replace position 2 with the value 2.
a=data.copy()
a[1]=12
a[2]=2
print(f'Part A:{process(a)[0]}')

# %%
