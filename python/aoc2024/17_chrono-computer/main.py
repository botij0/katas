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
    print(registers)
    program = parse_program(file_content)
    print(program)
    execute_program(registers, program)


def execute_program(registers: dict, program: list):
    i = 0
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
            print(INSTRUCTIONS[inst](registers["A"], operand), end=",")
            i += 1


def get_true_operand(registers: dict, operand: int, inst: int) -> int:
    inst_with_combo_op = [0, 2, 5, 6, 7]
    combo_op_regs = {4: "A", 5: "B", 6: "C"}
    if inst in inst_with_combo_op:
        return operand if operand < 4 else registers[combo_op_regs[operand]]
    return operand


def parse_registers(file_content: str) -> dict:
    registers = {}
    for line in file_content.splitlines():
        if line.startswith("Register"):
            register_name, register_value = line.split(":")
            registers[register_name.split()[-1]] = int(register_value)
    return registers


def parse_program(file_content: str) -> list:
    program = []
    program_line = file_content.splitlines()[-1].split(":")[-1].split(",")
    for i in range(0, len(program_line) - 1, 2):
        program.append((int(program_line[i]), int(program_line[i + 1])))
    return program


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
