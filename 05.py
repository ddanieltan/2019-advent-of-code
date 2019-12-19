# Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. 
# For example, the instruction 3,50 would take an input value and store it at address 50.
# Opcode 4 outputs the value of its only parameter. 
# For example, the instruction 4,50 would output the value at address 50.

#%% From Day 2
def intcode(input_):
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
        if check_if_opcode_single_digit(opcode):
            op1=output_[cursor+1]
            op2=output_[cursor+2]
            dest=output_[cursor+3]        
            if opcode==1:
                output_[dest]=output_[op1]+output_[op2]
                cursor+=4
            elif opcode==2:
                output_[dest]=output_[op1]*output_[op2]
                cursor+=4
            elif opcode==3:
                
            else:
                print(f'Error: {cursor}')
                break
    
    return output_

# %%
# Op codes 1 and 2 have 4 arguments
# Op codes 3 and 4 have 2 arguments
# Op code 99 ends the programme
# Op codes can be single digit or multiple digit
#%%
def check_if_intcode_single_digit(opcode):
    if len(str(opcode))==1:
        return True
    else:
        return False

# %%
def process_intcode(fullcode):
    output=fullcode.copy()
    cursor=0
    def process_opcode(opcode):
        if opcode==99:
            return
        if opcode==1: #addition
            p1=output[cursor+1]
            p2=output[cursor+2]
            dest=output[cursor+3]        
            output[dest]=output[p1]+output[p2]
            cursor+=4
            # elif opcode==2:
            #     output_[dest]=output_[op1]*output_[op2]
            #     cursor+=4
            # elif opcode==3:
                
            # else:
            #     print(f'Error: {cursor}')
            #     break
    
    while cursor < len(fullcode):
        intcode=fullcode[cursor]
        if len(str(intcode))==1:
            opcode=intcode
            process_opcode(opcode)
        else:
            opcode=int(str(intcode)[-2:])
            process_opcode(opcode)
    
    return output

#%%
a='1002'

#%%
b=['1','1','1','3']
process_intcode(b)

# %%
