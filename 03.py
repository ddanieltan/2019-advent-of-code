

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
            distance=abs(x)+abs(y)
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
i0=['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
i1=['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
l0=draw(i0)
l1=draw(i1)
man_dist=get_lowest_manh(set(l0) & set(l1))
print(man_dist)

# %% Part A

#%% input data
with open('data/03.dat') as f:
    data=f.readlines()

# %% answer
instruc0=data[0].split(',')
instruc1=data[1].split(',')

#%%
l0=draw(instruc0)
l1=draw(instruc1)
man_dist=get_lowest_manh(set(l0) & set(l1))
print(man_dist)

#%%
def get_lowest_steps(dict_coords,line):
    lowest_dist=9999999
    for i in dict_coords:
        if i==(0,0):
            continue
        else:
            for step,value in enumerate(line):
                if i==value:
                    print(i,value)
                    print(step)
                    if step<lowest_dist:
                        lowest_dist=step
                        print('lowest ',lowest_dist)
    
    return lowest_dist

#%%
def get_b_ans(dict_coords, line1,line2):
    a=get_lowest_steps(dict_coords,line1)
    b=get_lowest_steps(dict_coords,line2)
    return a+b

#%%
dict_coords=set(l0) & set(l1)
first_line_steps=get_lowest_steps(dict_coords,l0)
# second_line_steps=get_lowest_steps(dict_coords,l1)
# print(first_line_steps+second_line_steps)
# %% Test 1
i0=['R8','U5','L5','D3']
i1=['U7','R6','D4','L4']
l0=draw(i0)
l1=draw(i1)
dict_coords=set(l0) & set(l1)
get_b_ans(dict_coords,l0,l1)

#%% Test 2
i0=['R75','D30','R83','U83','L12','D49','R71','U7','L72']
i1=['U62','R66','U55','R34','D71','R55','D58','R83']
l0=draw_b(i0)
l1=draw_b(i1)
dict_coords=set(l0) & set(l1)
get_b_ans(dict_coords,l0,l1)


# %% 
def draw_b(instructions):
    coordinates=[(0,0)]
    for i in instructions:
        if i not in coordinates:
            coordinates=update(i,coordinates)
    return coordinates

# %% ANS from reddit

#%%
def calc_points_with_steps(path):
    curx = cury = step = 0
    directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
    points = {}
    for segment in path:
        dx, dy = directions[segment[0]]
        for _ in range(int(segment[1:])):
            curx += dx
            cury += dy
            step += 1
            if (curx, cury) not in points:
                points[(curx, cury)] = step
    return points

#%%
wire1_points = calc_points_with_steps(instruc0)
wire2_points = calc_points_with_steps(instruc1)
intersection_points = [point for point in wire1_points if point in wire2_points]

#%%
part1 = min(abs(x) + abs(y) for (x, y) in intersection_points)
part2 = min(wire1_points[point] + wire2_points[point] for point in intersection_points)

print('Part 1: {0}, Part 2: {1}'.format(part1, part2))

