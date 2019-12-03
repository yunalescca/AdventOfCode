import pandas as pd
import math

def day_3a():
    input = pd.read_csv('test2.txt', sep=',', header=None)
    wire1 = fill_coordinates([], input.loc[0])
    wire1_set = set(wire1)
    wire2 = fill_coordinates([], input.loc[1])
    min_dist = float('inf')
    for p2 in wire2:
        if p2 in wire1_set and p2 != (0,0):
            m_d = manhattan_distance((0,0), p2)
            if m_d < min_dist:
                min_dist = m_d
    
    print(min_dist)


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


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


day_3a()
