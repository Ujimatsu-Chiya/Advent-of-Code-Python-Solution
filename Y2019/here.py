from collections import deque, defaultdict


class IntCodeComputer:
    jmp = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]

    def __init__(self, program: list, input_array=[]):
        self.ops = defaultdict(int)
        self.sz = len(program)
        for i, x in enumerate(program):
            self.ops[i] = x
        self.pc = 0
        self.input = deque(input_array)
        self.output = deque()
        self.halt = False
        self.base = 0

    def get_pos(self, i, mod):
        return self.ops[i] if mod == 0 else i if mod == 1 else self.base + self.ops[i]

    def parse(self, opcode):
        s = "{:05}".format(opcode)
        return tuple(map(int, [s[3:], s[2], s[1], s[0]]))

    def run(self):
        while not self.halt:
            op, *mods = self.parse(self.ops[self.pc])
            idx = [self.get_pos(self.pc + i + 1, mods[i]) for i in range(3)]
            match op:
                case 1:
                    self.ops[idx[2]] = self.ops[idx[0]] + self.ops[idx[1]]
                case 2:
                    self.ops[idx[2]] = self.ops[idx[0]] * self.ops[idx[1]]
                case 3:
                    if len(self.input) == 0:
                        break
                    self.ops[idx[0]] = self.input.popleft()
                case 4:
                    self.output.append(self.ops[idx[0]])
                case 5:
                    if self.ops[idx[0]] != 0:
                        self.pc = self.ops[idx[1]]
                        continue
                case 6:
                    if self.ops[idx[0]] == 0:
                        self.pc = self.ops[idx[1]]
                        continue
                case 7:
                    self.ops[idx[2]] = int(self.ops[idx[0]] < self.ops[idx[1]])
                case 8:
                    self.ops[idx[2]] = int(self.ops[idx[0]] == self.ops[idx[1]])
                case 9:
                    self.base += self.ops[idx[0]]
                case 99:
                    self.halt = True
                    break
                case _:
                    assert False
            self.pc += self.jmp[op]

    def add_input(self, x):
        self.input.append(x)

    def get_output(self):
        if len(self.output) == 0:
            self.run()
        return self.output.popleft()

