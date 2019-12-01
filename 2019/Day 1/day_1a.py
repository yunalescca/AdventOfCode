import pandas as pd

def day_1a():
    input = pd.read_csv('input.txt', header=None)
    sum = 0
    for index,row in input.iterrows():
        value = int (row[0] / 3) - 2
        sum += value
    print(sum)

day_1a()