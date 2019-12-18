
start = 273025
#start =  111122
#end =    111123
end   = 767253

num = start
possiblePasscodes = []

# two adjacent numbers must be the same
# left to right, numbers must only increase

while num <= end:
    onlyIncrease = True
    twoAdjacentSame = False

    # if numbers only increase left to right
    numString = str(num)
    minNum = numString[0]
    for n in range(5):
        if numString[n] > numString[n+1]:
            onlyIncrease = False

    # two adjacent numbers must be the same and not part of a larger group
    numString = str(num)
    if numString[0] == numString[1] and numString[0] != numString[2]:
        twoAdjacentSame = True
    elif numString[1] == numString[2] and numString[1] != numString[0] and numString[1] != numString[3]:
        twoAdjacentSame = True
    elif numString[2] == numString[3] and numString[2] != numString[1] and numString[2] != numString[4]:
        twoAdjacentSame = True
    elif numString[3] == numString[4] and numString[3] != numString[2] and numString[3] != numString[5]:
        twoAdjacentSame = True
    elif numString[4] == numString[5] and numString[4] != numString[3]:
        twoAdjacentSame = True

    if onlyIncrease is True and twoAdjacentSame is True:
        possiblePasscodes.append(num)

    num += 1

print("There are", len(possiblePasscodes), "possible Passcodes")
print(possiblePasscodes)
