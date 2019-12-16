#%%
with open('data/03.dat') as f:
    data=f.readlines()

# %%
instruc0=data[0].split(',')
instruc1=data[1].split(',')

# %%
def update(instruction,coordinates):
    """
    Input: 1 Instruction eg. 'R75' (string),
    List of coordinates (tuple)
    Output: List of coordinates (tuples)
    """
    direction=instruction[0]
    distance=int(instruction[1:])

    latest_coord=coordinates[-1]
    if direction=="R":
        x,y=latest_coord
        for i in range(distance):
            new=(x+i+1,y)
            coordinates.append(new)
    if direction=="L":
        x,y=latest_coord
        for i in range(distance):
            new=(x-(i+1),y)
            coordinates.append(new)
    if direction=="U":
        x,y=latest_coord
        for i in range(distance):
            new=(x,y+i+1)
            coordinates.append(new)
    if direction=="D":
        x,y=latest_coord
        for i in range(distance):
            new=(x,y-(i+1))
            coordinates.append(new)
    
    return coordinates


# %%
#TEST
instruc_test=['R8','U5','L5','D3']


# %%
line_t=[(0,0)]
for i in instruc_test:
    line_t=update(i,line_t)

# %%
instruct_test_2=['U7','R6','D4','L4']
line_t2=[(0,0)]
for i in instruct_test_2:
    line_t2=update(i,line_t2)

# %%
set(instruc_test,instruct_test_2)

# %%
set(line_t) & set(line_t2)

# %%
def get_lowest_manh(dict_):
    lowest_dist=9999999
    coord=(16,12)
    for i in dict_:
        if i==(0,0):
            continue
        else:
            x,y=i
            distance=x+y
            if distance<lowest_dist:
                lowest_dist=distance
                coord=i
    
    return coord, lowest_dist


# %%
get_lowest_manh(set(line_t) & set(line_t2))

#%%
def draw(instructions):
    coordinates=[(0,0)]
    for i in instructions:
        coordinates=update(i,coordinates)
    return coordinates
# %%
#More Tests
i0=['R75','D30','R83','U83','L12','D49','R71','U7','L72']
i1=['U62','R66','U55','R34','D71','R55','D58','R83']
l0=draw(i0)
l1=draw(i1)
man_dist=get_lowest_manh(set(l0) & set(l1))
print(man_dist)

# %%
