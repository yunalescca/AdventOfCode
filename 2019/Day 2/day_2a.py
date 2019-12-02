
def day_2a():
    with open('input.txt', 'r') as f:
        input = f.read().split(',')
    input = list(map(int, input))

    input[1] = 12
    input[2] = 2

    i = 0
    while i < len(input):
        if input[i] == 1:
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
        elif input[i] == 2:
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
        elif input[i] == 99:
            print('Stop')
            break
        else:
            print('Invalid input')
            input[0] = (-1)
            break
        i += 4
    
    print(input[0])


day_2a()