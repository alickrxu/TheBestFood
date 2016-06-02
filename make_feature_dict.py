import pickle

def makeDict(fileName):
    fileLines = []
    dictionary = {}
    #make list of [restaraunt, features] pairs
    with open(fileName, 'r') as f:
        for line in f:
            fileLines.append(line.strip().split('|'))
    #seperate features into lists of their own
    for line in fileLines:
        line[0] = line[0].replace(" ","").lower()
        line[1] = line[1].replace(" ","").lower().split(',')
    #print fileLines
    #begin placing into nested dictionary
    temp = {}
    for line in fileLines:
        i = 0
        for subline in line[1]:
            temp[subline] = i
            i += 1
        dictionary[line[0]] = temp.copy()
        temp.clear()
    print dictionary
    with open("feature_dictionary.txt", "w") as f:
        pickle.dump(dictionary,f)


makeDict('features.txt')
