# Maybe save them all as tuples or something, figure out which one doesn't orbit anything else
# But I know it will be COM so at least I already know

def getInput(filename, objectDict, list):
    # Process input into a dictionary with orbited object as key
    input = open(filename, 'r')

    counter = 0

    for line in input:
        line = line.replace('\n',"")
        # Set up test list of first 10 items
        if counter <= 15:
            list.append(line[:len(line)])

        # If it's not already in the dict, add an entry, otherwise extend the value list
        orbitedObject = line[:line.find(")")]
        if orbitedObject not in objectDict:
            objectDict[orbitedObject] = [line[:len(line)]]
        else:
            objectDict[orbitedObject].append(line[:len(line)])

        counter+=1

    input.close()


def printTrace(objectDict, object, increment, count):

    # List of all objects orbiting given object
    entries = objectDict[object]

    # For each object in the list
    for orbitRelationship in entries:
        orbitee = orbitRelationship[orbitRelationship.find(")")+1:]
        # print(orbitRelationship, "count:", count, "increment:", increment)
        count += increment

        if orbitee in objectDict:
            count = printTrace(objectDict, orbitee, increment+1, count)

    return count

# assumes that start and end have nothing orbiting them
def calculateOrbitalPath(objectDict, start, end):
    # Find start YOU
    orbitWithYou = findOrbit(objectDict, start)
    orbited1 = orbitWithYou[:orbitWithYou.find(")")]
    #print(orbitWithYou)
    orbitWithSan = findOrbit(objectDict, end)
    orbited2 = orbitWithSan[:orbitWithSan.find(")")]
    #print(orbitWithSan)

    if orbitWithYou[:orbitWithYou.find(")")] == orbitWithSan[:orbitWithSan.find(")")]:
        print("They orbit the same")

    orbited1Stack = []

    # Trace the paths from start and end back to COM
    while orbited1 != "COM":
        nextOrbited = findOrbit(objectDict, orbited1)
        orbited1Stack.append(nextOrbited)
        orbited1 = nextOrbited[:nextOrbited.find(")")]

    #print(orbited1Stack)


    orbited2Stack = []

    # Trace the paths from start and end back to COM
    while orbited2 != "COM":
        nextOrbited = findOrbit(objectDict, orbited2)
        orbited2Stack.append(nextOrbited)
        orbited2 = nextOrbited[:nextOrbited.find(")")]

    #print(orbited2Stack)

    # find intersection point
    intersection = ""
    found = False
    while not found:
        for item in orbited1Stack:
            thing1 = item[:item.find(")")]
            for otherItem in orbited2Stack:
                thing2 = otherItem[:otherItem.find(")")]
                if thing1 == thing2:
                    intersection = thing1
                    found = True
                if found:
                    break
            if found:
                break

    #print(intersection)

    num1 = 0
    num2 = 0

    for item in orbited1Stack:
        num1 += 1
        if item[:item.find(")")] == intersection:
           break

    for item in orbited2Stack:
        num2 += 1
        if item[:item.find(")")] == intersection:
           break

    print(num1+num2)

def findOrbit(objectDict, satellite):

    for dictKey in objectDict:
        for item in objectDict[dictKey]:
            if item[item.find(")")+1:] != satellite:
                continue
            else:
                return item
        #print(dictKey, objectDict[dictKey])


def main(filename):
    # Dict for storing and organizing orbited values
    objectDict = {}

    # List of items for testing
    list = []

    # Process input into a set
    getInput(filename, objectDict, list)

    # Print saved list and lookup those items
    #print(list)
    #for item in list:
    #    print(item[:item.find(")")], objectDict[item[:item.find(")")]])

    #for dictKey in objectDict:
    #    print(dictKey, objectDict[dictKey])

    # Build tree by adding items in the correct order
    #print(printTrace(objectDict, 'COM', 1, 0))

    calculateOrbitalPath(objectDict, "YOU", "SAN")

main("input.txt")
