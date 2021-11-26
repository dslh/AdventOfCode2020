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
    individual_answers = groupsAnswers.split("\n")
    individual_sets = [set(x) for x in individual_answers]
    #print(individual_sets)
    #print(type(individual_sets))
    union = individual_sets[0]
    #print(union)
    #print(type(union))
    for x in individual_sets[1:]:
        union = union.intersection(x)
    #cleaned = individual_sets.intersection()
    #groupSet = set(withoutLines)
    #print(union)    
    return len(union)

print("Part 2:")

print(sum(howManyNewAnswers(x) for x in splitInput))
