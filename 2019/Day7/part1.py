import sys
import itertools

def main():
    file = open(input("Filename: "), 'r')
    intcodes = file.readline().split(',')
    intcodes = [int(x) for x in intcodes]

    final_outputs = {}
    for order in list(itertools.permutations(range(5))):
        output = 0
        for phase in order:
            output = intcode_computer(intcodes[:], [phase, output])
        final_outputs[output] = order
    
    # print(final_outputs)
    max_out = max(final_outputs)
    print(max_out, final_outputs[max_out])

def read_value(memory, mode, index):
    if mode == 0:
        return memory[memory[index]]
    else:
        return memory[index]

def write_value(memory, mode, index, write_value):
    if mode == 0:
        memory[memory[index]] = write_value
    else:
        memory[index] = write_value

def intcode_computer(intcodes, inputs):
    input_index = 0
    output = 0
    index = 0
    while True:
        opcode = intcodes[index] % 100
        a_mode = ( intcodes[index] % 1000 )   // 100
        b_mode = ( intcodes[index] % 10000 )  // 1000
        c_mode = ( intcodes[index] % 100000 ) // 10000

        if opcode == 1:
            a = read_value(intcodes, a_mode, index+1)
            b = read_value(intcodes, b_mode, index+2)
            write_value(intcodes, c_mode, index+3, a + b)
            index = index + 4

        elif opcode == 2:
            a = read_value(intcodes, a_mode, index+1)
            b = read_value(intcodes, b_mode, index+2)
            write_value(intcodes, c_mode, index+3, a * b)
            index = index + 4

        elif opcode == 3:
            write_value(intcodes, a_mode, index+1, inputs[input_index])
            input_index = input_index + 1
            index = index + 2

        elif opcode == 4:
            output = read_value(intcodes, a_mode, index+1)
            index = index + 2

        elif opcode == 5:
            if read_value(intcodes, a_mode, index+1) != 0:
                index = read_value(intcodes, b_mode, index+2)
            else:
                index = index + 3

        elif opcode == 6:
            if read_value(intcodes, a_mode, index+1) == 0:
                index = read_value(intcodes, b_mode, index+2)
            else:
                index = index + 3

        elif opcode == 7:
            a_value = read_value(intcodes, a_mode, index+1)
            b_value = read_value(intcodes, b_mode, index+2)
            if a_value < b_value:
                write_value(intcodes, c_mode, index+3, 1)
            else:
                write_value(intcodes, c_mode, index+3, 0)
            index = index + 4

        elif opcode == 8:
            a_value = read_value(intcodes, a_mode, index+1)
            b_value = read_value(intcodes, b_mode, index+2)
            if a_value == b_value:
                write_value(intcodes, c_mode, index+3, 1)
            else:
                write_value(intcodes, c_mode, index+3, 0)
            index = index + 4

        elif opcode == 99:
            break

    return output

main()