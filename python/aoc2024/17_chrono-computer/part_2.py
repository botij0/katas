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

INST_TO_REG = {
    0: {"op": "A", "res": "A"},
    1: {"op": "B", "res": "B"},
    2: {"op": "B", "res": "B"},
    6: {"op": "A", "res": "B"},
    7: {"op": "A", "res": "C"},
}


def main():
    file_content = read_file("puzzle_input.txt")
    registers = parse_registers(file_content)

    program = parse_program(file_content)
    expected_result = get_expected_result(program)
    print(program)
    print(expected_result)
    rega = get_rega_val(expected_result, program, registers)
    print(rega)


# A % 8 -> B
# B XOR x -> B
# A//2**B -> C
# B XOR C -> B
# B XOR C -> B
# A//2**3 -> A
# PRINT B % 8


def get_rega_val(expected_result, program, registers):
    result = []
    i = 8 ** (len(expected_result) - 1)
    its = 0
    while result != expected_result:
        i += (its * 8) + 2
        registers["A"] = i
        result = execute_program(registers, program, expected_result)
        its += 1
        # print(result)
    return i


def execute_program(registers, program, expected_result):
    i = 0
    result = []

    while i < len(program):
        inst, operand = program[i]
        operand = get_true_operand(registers, operand, inst)

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
            n = INSTRUCTIONS[inst](registers["A"], operand)
            result.append(n)
            if (
                len(result) > len(expected_result)
                or n != expected_result[result.index(n, -1)]
            ):
                result = []
                break
            i += 1
    return result


def get_expected_result(program):
    expected_result = []
    for pair in program:
        inst, operand = pair
        expected_result.append(inst)
        expected_result.append(operand)
    return expected_result


def get_true_operand(registers, op, inst):
    inst_with_combo_op = [0, 2, 5, 6, 7]
    combo_op_regs = {4: "A", 5: "B", 6: "C"}
    if inst in inst_with_combo_op:
        return op if op < 4 else registers[combo_op_regs[op]]
    return op


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
