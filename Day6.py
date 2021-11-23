#### Lines about lettercount in def howManyAnswers could be combined?
#### While loops for the length of something with a counter variable seems bloated. What's the shorter way?
#### Stuck on how to sum up the values in my dictionary
#Checking the number of letter replies
rawInput = """abc

a
b
c

ab
ac

a
a
a
a

b"""

splitInput = rawInput.split("\n\n") # Splitting the data into a list
print("splitInput = ")
print(splitInput)
numberOfGroups = len(splitInput) # Number of list groups
print(numberOfGroups)

def howManyAnswers(groupsAnswers): # This finds how many difference answers a group gave
    listedAns = groupsAnswers.split("\n") # Splits the groups answers into each row (person)
    #######dictLetters = {"a": 0, "b": 1, "c": 2} # Dictionary to remember numbers
    countLetters = {"a": 0, "b": 0, "c": 0} # Dictionary to count the # of letter occurances
    row = 0
    times = 0
    print("individual groups answers are ")
    print(listedAns)
    #print(countLetters)
    while row < len(listedAns):
        letterCount = 0
        #print("letterCount is ")
        #print(letterCount)
        line = listedAns[row]
        #print("line is ")
        #print(line)
        while letterCount < len(line):
            #print("letterCount is ")
            #print(letterCount)
            letter = line[letterCount]
            #print(letter)
            oldLetterCount = countLetters[letter] # Find letter value in dictionary
            if oldLetterCount == 0: oldLetterCount += 1 # Ensures values goes to 1 if 0, or stays at 1 if there
            #####newLetterCount = oldLetterCount + 1 # Add 1 to value
            countLetters.update({letter: oldLetterCount}) # Replace value in  dictionary
            letterCount +=1 # Move onto next letter in the row
        row +=1 # Move onto next row in the groupAnswers (next list entry in listedAns) 
    print("countLetters is ")
    print(countLetters)
    howMany = 0
    #for x < len(countLetters):
    #    pass
        #if countLetters
    #howMany = sum(intcountLetters) # Sums up the value of the countLetters dictionary, where they're either 0 or 1 #################Cycle dictionary to check how many have values >=1
    return howMany

sumQuestionCount = 0 # AoC question answer count initialised at 0
#print("sumQuestionCount is ")
#print(sumQuestionCount)

groupCount = 0 # Counting through the groups answers
#print("groupCount is ")
#print(groupCount)
while groupCount < numberOfGroups:
    ###### for x in splitInput: # Cycles through each list item (or each group's replies) of the data
    newAnswers = howManyAnswers(splitInput[groupCount]) # How many different letter answers did that group have
    sumQuestionCount = sumQuestionCount + newAnswers # Add this number to the total count
    groupCount += 1

print (sumQuestionCount)