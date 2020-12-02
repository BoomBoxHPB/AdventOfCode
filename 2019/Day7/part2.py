import sys
import itertools

def main():
    file = open(input("Filename: "), 'r')
    intcodes = file.readline().split(',')
    intcodes = [int(x) for x in intcodes]

    final_outputs = {}
    for order in list(itertools.permutations(range(5,10))):
        computers = []
        for phase in order:
            comp = Computer(intcodes)
            comp.Run(phase)
            computers.append(comp)

        output = 0
        while computers[len(computers)-1].IsRunning():
            for comp in computers:
                comp.Run(output)
                output = comp.GetOutput()

        final_outputs[output] = order
    
    # print(final_outputs)
    max_out = max(final_outputs)
    print(max_out, final_outputs[max_out])


class Computer:
    intcodes = None
    is_running = True
    output = 0
    index = 0

    def read_value(self, mode, index):
        if mode == 0:
            return self.intcodes[self.intcodes[index]]
        else:
            return self.intcodes[index]

    def write_value(self, mode, index, write_value):
        if mode == 0:
            self.intcodes[self.intcodes[index]] = write_value
        else:
            self.intcodes[index] = write_value

    def __init__(self, program):
        self.intcodes = program[:]
    
    def GetOutput(self):
        return self.output

    def IsRunning(self):
        return self.is_running

    def Run(self, input):
        input_used = False
        while True:
            opcode = self.intcodes[self.index] % 100
            a_mode = ( self.intcodes[self.index] % 1000 )   // 100
            b_mode = ( self.intcodes[self.index] % 10000 )  // 1000
            c_mode = ( self.intcodes[self.index] % 100000 ) // 10000

            if opcode == 1:
                a = self.read_value(a_mode, self.index+1)
                b = self.read_value(b_mode, self.index+2)
                self.write_value(c_mode, self.index+3, a + b)
                self.index = self.index + 4

            elif opcode == 2:
                a = self.read_value(a_mode, self.index+1)
                b = self.read_value(b_mode, self.index+2)
                self.write_value(c_mode, self.index+3, a * b)
                self.index = self.index + 4

            elif opcode == 3:
                if input_used:
                    return
                self.write_value(a_mode, self.index+1, input)
                input_used = True
                self.index = self.index + 2

            elif opcode == 4:
                self.output = self.read_value(a_mode, self.index+1)
                self.index = self.index + 2

            elif opcode == 5:
                if self.read_value(a_mode, self.index+1) != 0:
                    self.index = self.read_value(b_mode, self.index+2)
                else:
                    self.index = self.index + 3

            elif opcode == 6:
                if self.read_value(a_mode, self.index+1) == 0:
                    self.index = self.read_value(b_mode, self.index+2)
                else:
                    self.index = self.index + 3

            elif opcode == 7:
                a_value = self.read_value(a_mode, self.index+1)
                b_value = self.read_value(b_mode, self.index+2)
                if a_value < b_value:
                    self.write_value(c_mode, self.index+3, 1)
                else:
                    self.write_value(c_mode, self.index+3, 0)
                self.index = self.index + 4

            elif opcode == 8:
                a_value = self.read_value(a_mode, self.index+1)
                b_value = self.read_value(b_mode, self.index+2)
                if a_value == b_value:
                    self.write_value(c_mode, self.index+3, 1)
                else:
                    self.write_value(c_mode, self.index+3, 0)
                self.index = self.index + 4

            elif opcode == 99:
                self.is_running = False
                return


main()