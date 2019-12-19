#%% https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/day06.py
import collections

# %%
class Node:
    def __init__(self,code):
        self.code=code
        self.root=True
        self.children =[]

# %%
def build_orbit_graph(orbit_map):
    orbit_graph={}
    for left,right in map(lambda x:x.split(')'),orbit_map):
        if left not in orbit_graph:
            orbit_graph[left]=Node(left)
        if right not in orbit_graph:
            orbit_graph[right]=Node(right)
        orbit_graph[right].root=False
        orbit_graph[left].children.append(orbit_graph[right])
        orbit_graph[right].children.append(orbit_graph[left])
    return orbit_graph

#%% crazy function! Can't follow
def count_checksums(graph):
    seen=set()
    def traverse(node,depth=0):
        if node.code in seen:
            return 0
        seen.add(node.code)
        return depth+sum(traverse(child,depth+1) for child in node.children)
    return sum(traverse(node) for node in graph.values() if node.root)

#%%
test_input=['VTH)PD7',
'9H9)N65',
'YNL)2N6',
'JV2)CJM',
'M5C)7G7']

# %%
build_orbit_graph(test_input)
#%%
count_checksums(build_orbit_graph(test_input))
# %%
with open('data/06.dat') as f:
    data=f.readlines()
data = [x.strip('\n') for x in data]


# %% Part 1
orbit_graph=build_orbit_graph(data)


# %%
count_checksums(orbit_graph)

# %% Part 2
def minimum_transfers(graph,source,destination):
    queue=collections.deque([(graph[source],0)])
    seen={source:0}
    while destination not in seen:
        node,depth=queue.pop()
        for child in node.children:
            if child.code not in seen:
                seen[child.code] = depth+1
                queue.append((child,depth+1))
    return seen[destination]-2


# %%
minimum_transfers(orbit_graph,'YOU','SAN')

# %%
