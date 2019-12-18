
start = 273025
#start =  333333
#end =    333339
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

    # two adjascent numbers must be the same
    numString = str(num)
    minNum = numString[0]
    for n in range(5):
        if numString[n] == numString[n+1]:
            twoAdjacentSame = True

    if onlyIncrease is True and twoAdjacentSame is True:
        possiblePasscodes.append(num)

    num += 1

print("There are", len(possiblePasscodes), "possible Passcodes")
print(possiblePasscodes[0], possiblePasscodes[1], possiblePasscodes[2], )
