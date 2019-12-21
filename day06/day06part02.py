# Maybe save them all as tuples or something, figure out which one doesn't orbit anything else
# But I know it will be COM so at least I already know

def getInput(filename, objectDict, list):
    # Process input into a dictionary with orbited object as key
    input = open(filename, 'r')

    counter = 0

    for line in input:
        line = line.replace('\n',"")
        # Set up test list of first 10 items
        if counter <= 11:
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
    #    print(item[:3], objectDict[item[:3]])

    # Build tree by adding items in the correct order
    print(printTrace(objectDict, 'COM', 1, 0))

main("input.txt")
