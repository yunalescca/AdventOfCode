
def day_2b():
    with open('input.txt', 'r') as f:
        input = f.read().split(',')
    input = list(map(int, input))
    saved_input = input.copy()

    for k in range (0,100):
        input = saved_input.copy()
        for j in range (0,100):
            input = saved_input.copy()
            input[1] = k
            input[2] = j

            i = 0
            while i < len(input) and input[0] != 19690720:
                if input[i] == 1:
                    input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
                elif input[i] == 2:
                    input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
                elif input[i] == 99: # stop
                    break
                else: # invalid input
                    input[0] = (-1)
                    break
                i += 4
            
            if input[0] == 19690720:
                break
        
        if input[0] == 19690720:
            break
    
    print(input[0])
    print(100 * input[1] + input[2])

day_2b()