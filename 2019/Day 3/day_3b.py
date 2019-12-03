import pandas as pd
import math

def day_3b():
    input = pd.read_csv('input.txt', sep=',', header=None)
    wire1 = fill_coordinates([], input.loc[0])
    wire1_set = set(wire1)
    wire2 = fill_coordinates([], input.loc[1])
    min_steps = float('inf')
    for p2 in wire2:
        if p2 in wire1_set and p2 != (0,0):
            steps = wire1.index(p2) + wire2.index(p2)
            if steps < min_steps:
                min_steps = steps
    
    print(min_steps)


def fill_coordinates(wire, input):
    wire.append((0,0))
    direction = { 
        'R': (1, 0), 
        'L': (-1, 0), 
        'U': (0, 1), 
        'D': (0, -1) 
    }
    i=0
    for a in input:
        if a != a:
            break
        dist = int(a[1:])
        change = direction[a[0]]
        for d in range(0,dist):
            wire.append((wire[i][0] + change[0],
                        wire[i][1] + change[1]))
            i+=1
            
    return wire

day_3b()
