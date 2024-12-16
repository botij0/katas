/*
Para ayudarles, vamos a implementar un intérprete sencillo que soporte las siguientes instrucciones mágicas:

MOV x y: Copia el valor x (puede ser un número o el contenido de un registro) en el registro y
INC x: Incrementa en 1 el contenido del registro x
DEC x: Decrementa en 1 el contenido del registro x
JMP x y: Si el valor del registro x es 0 entonces salta a la instrucción en el índice y y sigue ejecutándose el programa desde ahí.
Comportamiento esperado:
Si se intenta acceder, incrementar o decrementar a un registro que no ha sido inicializado, se tomará el valor 0 por defecto.
El salto con JMP es absoluto y lleva al índice exacto indicado por y.
Al finalizar, el programa debe devolver el contenido del registro A. Si A no tenía un valor definido, retorna undefined.
*/

function compile(instructions: string[]): number | undefined {
    let registers: Record<string, number> = {};

    const getValue = (operand: string): number =>
        isNaN(Number(operand)) ? registers[operand] ?? 0 : Number(operand);

    const setRegister = (register: string, value: number): void => {
        registers[register] = value;
    };

    let i = 0;
    while (i < instructions.length) {
        const [command, arg1, arg2] = instructions[i].split(" ");
        switch (command) {
            case "MOV":
                setRegister(arg2, getValue(arg1));
                break;

            case "INC":
                setRegister(arg1, getValue(arg1) + 1);
                break;

            case "DEC":
                setRegister(arg1, getValue(arg1) - 1);
                break;

            case "JMP":
                if (getValue(arg1) === 0) {
                    i = Number(arg2);
                    continue;
                }
                break;

            default:
                throw new Error(`Comando desconocido: ${command}`);
        }
        i++;
    }
    return registers["A"];
}

const instructions = [
    "MOV -1 C", // copia -1 al registro 'C',
    "INC C", // incrementa el valor del registro 'C'
    "JMP C 1", // salta a la instrucción en el índice 1 si 'C' es 0
    "MOV C A", // copia el registro 'C' al registro 'a',
    "INC A", // incrementa el valor del registro 'a'
];

console.log(compile(instructions)); // -> 2
