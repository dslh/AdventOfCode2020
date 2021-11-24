from get_aoc import get_input

rawInput = get_input(4)

splitInput = rawInput.split("\n\n") # Splitting the data into a list
print("splitInput = ")
numberOfPP = len(splitInput) # Number of list entries/passports
print(numberOfPP)

######piste = len(split_input[0]) # Width of trees
######print(piste)

numCorrectPP = 0 # Counter for answer at the end
ppNum = 0 # Current passport number/list entry
########horiPos = 0 # Where across that line/list entry the toboggan is
print(numCorrectPP, ppNum)

while ppNum < numberOfPP: #Check each passport
    currentPP = splitInput[ppNum] # Get's the line/passport
    #print(currentPP)
    
    i = 0
    for x in currentPP: #Checks to see how many entries are in the passport
        if x == ":": i += 1 # Counts the number of ':'
    
    if i == 8: #If * it's a correct passport
        numCorrectPP += 1
        print("found a 8 entry passport, so it's valid")
    elif i == 7: # Else if 7 then it has to contain cid
        if "cid" in currentPP:
            print("found a 7 entry passport with cid, so it doesn't count")
        else:
            numCorrectPP += 1
            print("found a 7 entry passport without cid, so it's valid")
    ppNum += 1
    
print(numCorrectPP)
