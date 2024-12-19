# Inst
# 0 - Division A/x^2 -> A
# 1 - B XOR x -> B
# 2 - combo x -> B
# 3 - if A!=0 goto x
# 4 - B XOR C -> B
# 5 - combo x -> output
# 6 - Division A/x^2 -> B
# 7 - Division A/x^2 -> C

INSTRUCTIONS = {
    0: lambda a, x: a // 2**x,
    1: lambda b, x: b ^ x,
    2: lambda _, x: x % 8,
    4: lambda b, c: b ^ c,
    5: lambda _, x: x % 8,
    6: lambda a, x: a // 2**x,
    7: lambda a, x: a // 2**x,
}

OPERANDS = {
    4: "A",
    5: "B",
    6: "C",
}

INST_TO_REG = {
    0: {"op": "A", "res": "A"},
    1: {"op": "B", "res": "B"},
    2: {"op": "B", "res": "B"},
    6: {"op": "A", "res": "B"},
    7: {"op": "A", "res": "C"},
}

NEEDS_COMB_OP = [0, 2, 5, 6, 7]


def main():
    file_content = read_file("puzzle_input.txt")
    registers = parse_registers(file_content)
    print(registers)
    program = parse_program(file_content)
    print(program)
    execute_program(registers, program)
    print()
    print(registers)


def execute_program(registers, program):
    i = 0
    while i < len(program):
        inst, operand = program[i]
        if inst in NEEDS_COMB_OP:
            operand = operand if operand < 4 else registers[OPERANDS[operand]]

        if inst in INST_TO_REG:
            registers[INST_TO_REG[inst]["res"]] = INSTRUCTIONS[inst](
                registers[INST_TO_REG[inst]["op"]], operand
            )
            i += 1
        elif inst == 4:
            registers["B"] = INSTRUCTIONS[inst](registers["B"], registers["C"])
            i += 1
        elif inst == 3:
            if registers["A"] != 0:
                i = operand
            else:
                i += 1
        elif inst == 5:
            print(INSTRUCTIONS[inst](registers["A"], operand), end=",")
            i += 1


def parse_registers(file_content):
    registers = {}
    for line in file_content.splitlines():
        if line.startswith("Register"):
            register_name, register_value = line.split(":")
            registers[register_name.split()[-1]] = int(register_value)
    return registers


def parse_program(file_content):
    program = []
    program_line = file_content.splitlines()[-1]
    program_line = program_line.split(":")[-1].split(",")
    for i in range(0, len(program_line) - 1, 2):
        program.append((int(program_line[i]), int(program_line[i + 1])))
    return program


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
