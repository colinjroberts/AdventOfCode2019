
#Various inputs
test1 = "3,0,4,0,99" #Takes input and prints it
test2 = "1,2,3,1,99" #Add value at index 2 and value at index 3 save in index 1
test3 = "2,2,0,1,99" #Multiple value at index 2 and value at index 0, save in index 1
test4 = "11101,2,3,1,2,4,4,0,99"
test5 = "1002,4,3,4,33"
test6 = "1101,100,-1,4,0"

part1 = "3,225,1,225,6,6,1100,1,238,225,104,0,1002,36,25,224,1001,224,-2100,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,31,84,225,1102,29,77,225,1,176,188,224,101,-42,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,2,196,183,224,1001,224,-990,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,102,14,40,224,101,-1078,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1001,180,64,224,101,-128,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,24,17,224,1001,224,-408,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,9,66,224,1001,224,-75,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1102,18,33,225,1101,57,64,225,1102,45,11,225,1101,45,9,225,1101,11,34,225,1102,59,22,225,101,89,191,224,1001,224,-100,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,7,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,8,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,677,226,224,1002,223,2,223,1005,224,464,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,494,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,509,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,539,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,554,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,629,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,644,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226"

# Runs an instruction and returns location of next instruction
def runInstruction(instructions, x, debugMode):
    if debugMode is True:
        print("beginning instruction at location", x, "using", instructions)
    instructionLoc = x

    # parse opcode and parameters
    instruction = instructions[x]
    opcodeStr = str(instruction)

    while(len(opcodeStr)) < 5:
        opcodeStr = '0' + opcodeStr

    opcode = int(opcodeStr[3:])
    param1mode = int(opcodeStr[2])
    param2mode = int(opcodeStr[1])
    param3mode = int(opcodeStr[0])

    if debugMode is True:
        print("instruction is", opcodeStr, "and opcode is", opcode, "| param1:", param1mode,
              "param2:", param2mode, "param3:", param3mode)

    # opcode 1 adds 2 values after 2 and stores at 3rd value after 2
    # opcode 2 multiples 2 values after 2 and stores at 3rd value after 2
    if(opcode == 1 or opcode == 2):
        operand1 = 0
        operand2 = 0

        if param1mode == 0:
            operand1val = instructions[(x+1)]
            operand1 = instructions[operand1val]
        elif param1mode == 1:
            operand1 = instructions[(x+1)]

        if param2mode == 0:
            operand2val = instructions[(x + 2)]
            operand2 = instructions[operand2val]
        elif param2mode == 1:
            operand2 = instructions[(x + 2)]

        opcode12saveLoc = instructions[x+3]

        if (opcode == 1):
            instructions[opcode12saveLoc] = operand1 + operand2
            if debugMode is True:
                print("added", operand1, "and", operand2, "and saved in location", opcode12saveLoc)
                print("opcode 1 results in:", instructions, '\n')

        else:
            instructions[opcode12saveLoc] = operand1 * operand2
            if debugMode is True:
                print("multiplied", operand1, "and", operand2, "and saved in location", opcode12saveLoc)
                print("opcode 2 results in:", instructions, '\n')

        return x + 4

    # opcode 3 takes input, stores at location following 3
    if(opcode == 3):
        inputValue = int(input("Provide input: "))
        opcode3saveLoc = instructions[x+1]
        instructions[opcode3saveLoc] = inputValue

        if debugMode is True:
            print("opcode 3 results in:", instructions, '\n')

        return x + 2

    # opcode 4 gets value from location following 4 and prints it
    if(opcode == 4):
        if param1mode == 0:
            opcode4retreiveLoc = instructions[x + 1]
            outputValue = instructions[opcode4retreiveLoc]
        elif param1mode == 1:
            outputValue = instructions[x + 1]

        print(outputValue)

        if debugMode is True:
            print("opcode 4 results in:", instructions, '\n')

        return x + 2

    if(instruction == 99):
        return -1

    else:
        print("Error: encountered opcode:", instruction)
        return -1

def main(values):
    DEBUGFLAG = False
    instructions = values.split(",")
    instructions = [int(instruction) for instruction in instructions]

    result = runInstruction(instructions, 0, DEBUGFLAG)

    while (result != -1):
        result = runInstruction(instructions, result, DEBUGFLAG)

main(part1)
