ADD = '01'
MUL = '02'
INPUT = '03'
OUTPUT = '04'
STOP = '99'

PROGRAM_INPUT = 1

class IntCode:

    def __init__(self):
        with open('input.txt', 'r') as f:
            program = f.read().split(',')
        self.program = list(map(int, program))
        self.ip = 0
        self.stopped = False
        self.opcode_map = {
            ADD: (self.op_add, 2),
            MUL: (self.op_mul, 2),
            INPUT: (self.op_input, 1),
            OUTPUT: (self.op_output, 1),
            STOP: (self.op_stop, 0)
        }
        

    def run(self):
        while self.ip < len(self.program) and not self.stopped:
            instruction = str(self.program[self.ip]).zfill(5)
            opcode = instruction[-2:]
            func, nr_params = self.opcode_map[opcode]
            values = self.get_values(instruction, nr_params)
            steps = func(values)
            self.ip += steps
        

    def position_or_immediate(self, param_mode, param_index):
        parameter = self.program[self.ip + param_index]
        if param_mode == '0': # position mode
            return self.program[parameter]
        return parameter # immediate mode
    

    def get_values(self, instruction, nr_params):
        values = []
        for i in range(nr_params):
            values.append(self.position_or_immediate(instruction[2 - i], i + 1))
        return values


    def op_add(self, values):
        self.program[self.program[self.ip + 3]] = values[0] + values[1]
        return 4
    

    def op_mul(self, values):
        self.program[self.program[self.ip + 3]] = values[0] * values[1]
        return 4


    def op_input(self, values):
        self.program[self.program[self.ip + 1]] = PROGRAM_INPUT
        return 2


    def op_output(self, values):
        print(values[0])
        return 2

    
    def op_stop(self, instruction):
        self.stopped = True
        return 0


a = IntCode().run()