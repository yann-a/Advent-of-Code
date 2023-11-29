from collections import defaultdict
import copy

class NoMoreInput(Exception):
    pass

class WrongProgramPos(Exception):
    pass

class WrongMode(Exception):
    pass

class IntCodeProgram():
    def __init__(self, program, input=[]):
        self.program = defaultdict(int)
        for i in range(len(program)): self.program[i] = program[i]
        self.input = input
        self.output = []
        self.pc = 0
        self.relative_base = 0

    def getpos(self, pos, mode):
        if mode == 0: return self.program[pos]
        elif mode == 1: return pos
        elif mode == 2: return self.relative_base + self.program[pos]
        else: raise WrongMode

    def getvalue(self, pos, mode):
        return self.program[self.getpos(pos, mode)]
        
    def exec_one(self):
        full_inst = self.program[self.pc]
        inst, modes = full_inst % 100, full_inst // 100
        if inst == 1:
            self.program[self.getpos(self.pc + 3, (modes // 100) % 10)] = self.getvalue(self.pc + 1, modes % 10) + self.getvalue(self.pc + 2, (modes // 10) % 10)
            self.pc += 4
        elif inst == 2:
            self.program[self.getpos(self.pc + 3, (modes // 100) % 10)] = self.getvalue(self.pc + 1, modes % 10) * self.getvalue(self.pc + 2, (modes // 10) % 10)
            self.pc += 4
        elif inst == 3:
            if len(self.input) == 0: raise NoMoreInput
            self.program[self.getpos(self.pc + 1, modes % 10)] = self.input.pop(0)
            self.pc += 2
        elif inst == 4:
            self.output.append(self.getvalue(self.pc + 1, modes % 10))
            self.pc += 2
        elif inst == 5:
            if self.getvalue(self.pc + 1, modes % 10) != 0:
                self.pc = self.getvalue(self.pc + 2, (modes // 10) % 10)
            else:
                self.pc += 3
        elif inst == 6:
            if self.program[self.getpos(self.pc + 1, modes % 10)] == 0:
                self.pc = self.getvalue(self.pc + 2, (modes // 10) % 10)
            else:
                self.pc += 3
        elif inst == 7:
            if self.getvalue(self.pc + 1, modes % 10) < self.getvalue(self.pc + 2, (modes // 10) % 10):
                self.program[self.getpos(self.pc + 3, (modes // 100) % 10)] = 1
            else:
                self.program[self.getpos(self.pc + 3, (modes // 100) % 10)] = 0
            self.pc += 4
        elif inst == 8:
            if self.getvalue(self.pc + 1, modes % 10) == self.getvalue(self.pc + 2, (modes // 10) % 10):
                self.program[self.getpos(self.pc + 3, (modes // 100) % 10)] = 1
            else:
                self.program[self.getpos(self.pc + 3, (modes // 100) % 10)] = 0
            self.pc += 4
        elif inst == 9:
            self.relative_base += self.getvalue(self.pc + 1, modes % 10)
            self.pc += 2
        elif inst == 99: return True
        else: raise WrongProgramPos

    def addInput(self, new_input):
        self.input.append(new_input)

    def getOutput(self):
        return self.output.pop(0) if len(self.output) > 0 else None

    def run(self):
        try:
            while self.exec_one() is None:
                pass
            return True
        except NoMoreInput:
            return False

    def copy(self):
        return copy.deepcopy(self)