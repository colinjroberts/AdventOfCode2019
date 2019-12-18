# This script defines a program for processing intcode then brute forces a search for particular input parameters that 
# result in a particular output

# Various Test inputs
#inputTest = [1,9,10,3,2,3,11,0,99,30,40,50]
#inputTest = [1,0,0,0,99]
#inputTest = [2,3,0,3,99]
#inputTest = [2,4,4,5,99,0]
#inputTest = [1,1,1,4,99,5,6,0,99]

# Read in a text file with input
inputfile = open("input.txt", "r")
inputString = inputfile.read()
inputfile.close()
input = inputString.split(",")

#input = inputTest #If using test values instead

# Make sure all values are integers
input = [int(item) for item in input]

# Set values in positions 1 and 2 as the passed parameters
def runProgram(param1, param2):
    # Initialize the "program" as the provided input, change values 1 and 2, initialize opcode
    program = input.copy()
    program[1] = param1
    program[2] = param2
    opcode = program[0]
    
    #opround is the number of times the program has looped
    opround = 0

    # Loop as long as 99 has not been passed and as lone as op codes are valid
    while(opcode != 99 and (opcode == 1 or opcode == 2)):
        edit = program[3+4*opround]
        opval1 = program[1+4*opround]
        opval2 = program[2+4*opround]

        if opcode == 1:
            program[edit] = program[opval1] + program[opval2]
        elif opcode == 2:
            program[edit] = program[opval1] * program[opval2]

        opround+=1
        opcode = program[4*opround]

    return program[0]


# Part 1: Restore gravity by replacing position 1 with value 12 and position 2 with value 2
# print(runProgram(12, 2))


# Part 1 - Print the full results to a file just to have
# output = open("output.txt", "w+")
# for index in range(len(input)):
#     output.write(str(input[index]))
#     if (index != len(input)-1):
#         output.write(",")
# output.close()


# Part 2 - Try various initial values until you get a desired result
# desiredResults = 6730673 #Try value from part 1 to make sure def is working
desiredResults = 19690720
solutionFound = False

for x in range(50):
    for y in range(50):
        if(not solutionFound):
            result = runProgram(x, y)
            #print(result)
            if result == desiredResults:
                print("Inputs", x, y, "result in desired output:", desiredResults)
                print("100 * noun + verb =", 100*x+y)
                solutionFound = True
  
if(not solutionFound):
    print("No solution was found.")
