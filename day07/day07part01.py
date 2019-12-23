from itertools import permutations

output = 0

# Runs an instruction and returns location of next instruction
def runInstruction(instructions, x, debugMode, input1, input2):
    global OUTPUT
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
        if input == -1:
            inputValue = int(input("Provide input:"))
        else:
            inputValue = input1
            if debugMode is True:
                print("opcode 3 used value:", inputValue, '\n')
        opcode3saveLoc = instructions[x+1]
        instructions[opcode3saveLoc] = inputValue

        if debugMode is True:
            print("opcode 3 results in:", instructions, '\n')

        return x + 2

    # opcode 4 gets value from location following 4 and prints it
    if(opcode == 4):
        global output
        if param1mode == 0:
            opcode4retreiveLoc = instructions[x + 1]
            outputValue = instructions[opcode4retreiveLoc]
        elif param1mode == 1:
            outputValue = instructions[x + 1]

        if debugMode is True:
            print("saving output value:", outputValue)
        output = outputValue
        #print(outputValue)

        if debugMode is True:
            print("opcode 4 results in:", instructions, '\n')

        return x + 2

    # opcode 5 jumps pointer if non-zero, opcode 6 jumps if 0
    if opcode == 5 or opcode==6:
        operand1 = 0
        operand2 = 0

        if param1mode == 0:
            operand1val = instructions[(x + 1)]
            operand1 = instructions[operand1val]
        elif param1mode == 1:
            operand1 = instructions[(x + 1)]

        if param2mode == 0:
            operand2val = instructions[(x + 2)]
            operand2 = instructions[operand2val]
        elif param2mode == 1:
            operand2 = instructions[(x + 2)]

        if opcode == 5:
            if operand1 != 0:
                if debugMode is True:
                    print("about to return", operand2)
                    print("opcode 5 results in:", instructions, '\n')
                return operand2
            else:
                if debugMode is True:
                    print("not returning a number")
                    print("opcode 5 results in:", instructions, '\n')
                return x+3
        else:
            if operand1 == 0:
                if debugMode is True:
                    print("about to return", operand2)
                    print("opcode 6 results in:", instructions, '\n')
                return operand2
            else:
                if debugMode is True:
                    print("not returning a number")
                    print("opcode 6 results in:", instructions, '\n')
                return x+3

    # opcode 7 returns 1 if operand 1 < operand2, 0 otherwise
    # opcode 8 returns 1 if operand1 == operand2, 0 otherwise
    if opcode == 7 or opcode == 8:
        operand1 = 0
        operand2 = 0

        if param1mode == 0:
            operand1val = instructions[(x + 1)]
            operand1 = instructions[operand1val]
        elif param1mode == 1:
            operand1 = instructions[(x + 1)]

        if param2mode == 0:
            operand2val = instructions[(x + 2)]
            operand2 = instructions[operand2val]
        elif param2mode == 1:
            operand2 = instructions[(x + 2)]

        opcode78saveLoc = instructions[x+3]

        if opcode == 7:
            if operand1 < operand2:
                instructions[opcode78saveLoc] = 1
                if debugMode is True:
                    print(operand1, "is less than", operand2, "; storing 1 in", opcode78saveLoc)
                    print("opcode 7 results in:", instructions, '\n')
            else:
                instructions[opcode78saveLoc] = 0
                if debugMode is True:
                    print(operand1, "is not less than", operand2, "; storing 0 in", opcode78saveLoc)
                    print("opcode 7 results in:", instructions, '\n')
            return x+4
        else:
            if operand1 == operand2:
                instructions[opcode78saveLoc] = 1
                if debugMode is True:
                    print(operand1, "is equal to", operand2, "; storing 1 in", opcode78saveLoc)
                    print("opcode 8 results in:", instructions, '\n')
            else:
                instructions[opcode78saveLoc] = 0
                if debugMode is True:
                    print(operand1, "is not equal to", operand2, "; storing 0 in", opcode78saveLoc)
                    print("opcode 8 results in:", instructions, '\n')
            return x+4

    if opcode == 99:
        return -1

    else:
        print("Error: encountered opcode:", instruction)
        return -1

# Performs an intocde run with a set of instructions, two input variables, and an output collector
def runIntcode(inputValues, phaseSettings, debug, input1, input2):
    DEBUGFLAG = debug
    instructions = inputValues.split(",")
    instructions = [int(instruction) for instruction in instructions]

    if debug is True:
        print("calling runIntcode with input1:", input1, input2)

    result = runInstruction(instructions, 0, DEBUGFLAG, input1, input2)
    result = runInstruction(instructions, result, DEBUGFLAG, input1, input2)

    # HERE NEED TO MAKE IT SO A VALUE OF 3 USES THE FIRST INPUT THEN THE SECOND

    while (result != -1):
        result = runInstruction(instructions, result, DEBUGFLAG, -1)


def runAmpSequence(inputValues, phaseSettings, debug):
    global output
    DEBUGFLAG = debug

    #Process instructions
    instructions = inputValues.split(",")
    instructions = [int(instruction) for instruction in instructions]

    # Process phase order
    phases = []
    for n in range(5):
        phases.append(int(phaseSettings[n]))
    if debug is True:
        print(phases)

    # Run the program 5 times using output values as you go
    for n in range(len(phases)):
        if debug is True:
            print("phase[", n, "] input:", phases[n])

        runIntcode(inputValues, phaseSettings, debug, phases[n], output)

        if debug is True:
            print("output:", output)

    # Print final output
    if debug is True:
        print("final output:", output)
    #print("final output:", output)
    return output

def main(inputValues, debug):
    maxOutput = 0

    # Assemble phase settings
    seq = permutations([0, 1, 2, 3, 4])
    phaseSettings = ''
    for p in list(seq):
        inputstr = ''
        for item in p:
            inputstr += str(item)
        phaseSettings = inputstr
        if debug:
            print(inputstr)
        global output
        output = 0
        if inputstr == '01234':
            maxOutput = max(maxOutput, runAmpSequence(inputValues, phaseSettings, debug))

    print(inputValues)
    print(maxOutput)

#Various inputs
test1 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0" #43210
test2 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0" #54321
test3 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0" #65210
inputVals = "3,8,1001,8,10,8,105,1,0,0,21,46,59,80,105,122,203,284,365,446,99999,3,9,102,3,9,9,1001,9,5,9,102,2,9,9,1001,9,3,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,102,4,9,9,101,3,9,9,102,2,9,9,4,9,99,3,9,102,5,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99"

main(inputVals,True)


