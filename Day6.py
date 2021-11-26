#### Lines about lettercount in def howManyAnswers could be combined?
#### While loops for the length of something with a counter variable seems bloated. What's the shorter way?
#### Stuck on how to sum up the values in my dictionary
#Checking the number of letter replies
from get_aoc import get_input

rawInput = get_input(6)

splitInput = rawInput.split("\n\n") # Splitting the data into a list
print("splitInput = ")
print(splitInput)
print(len(splitInput)) # Number of list groups

def howManyAnswers(groupsAnswers): # This finds how many difference answers a group gave
    #without_line = groupsAnswers.strip() # Why didn't this strip function work?
    withoutLines = groupsAnswers.replace("\n","")
    groupSet = set(withoutLines)
    return len(groupSet)

print("Part 1:")
print(sum(howManyAnswers(x) for x in splitInput))

def howManyNewAnswers(groupsAnswers): # This finds how many identical answers a group gave
    sets = [set(answers) for answers in groupsAnswers.split()]
    return len(sets[0].intersection(*sets[1:]))

print("Part 2:")

print(sum(howManyNewAnswers(x) for x in splitInput))
