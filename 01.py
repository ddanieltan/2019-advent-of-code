#%%
import math

#Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass, divide by three, 
# round down, and subtract 2.

#%%
def fuel(mass):
    return math.floor(mass/3)-2

# %%
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

#%%
assert fuel(12)==2
assert fuel(14)==2
assert fuel(1969)==654
assert fuel(100756)==33583

#%%
data = [line.rstrip() for line in open('data/01.dat')]

# %% Part A
ans_a=0
for i in data:
    ans_a+=fuel(int(i))
print(ans_a)


# %% Part B
ans_b=0
for i in data:
    f=fuel(int(i))
    while f>0:
        ans_b+=f
        f=fuel(f)
print(ans_b)
