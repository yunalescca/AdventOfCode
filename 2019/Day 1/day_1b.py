import pandas as pd

def day_1b():
    input = pd.read_csv('input.txt', header=None)
    sum = 0
    for index,row in input.iterrows():
        sum += calculate_total_fuel(row[0])
    print(sum)


def calculate_total_fuel(val):
    if val < 9:
        return 0
    else:
        res = int (val / 3) - 2
        res += calculate_total_fuel(res)
        return res
        
day_1b()