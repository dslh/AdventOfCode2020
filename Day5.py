#Checking the boarding pass number

from get_aoc import get_input

rawInput = get_input(5)

splitInput = rawInput.split("\n") # Splitting the data into a list

def findRow(rowCode): # This finds the row number from the 7 letter row code
    row = 0
    if rowCode[0] == "B": row += 64
    if rowCode[1] == "B": row += 32
    if rowCode[2] == "B": row += 16
    if rowCode[3] == "B": row += 8
    if rowCode[4] == "B": row += 4
    if rowCode[5] == "B": row += 2
    if rowCode[6] == "B": row += 1
    return row
    
def findColumn(colCode): # This finds the column seat number from the 3 letter column code
    col = 0
    if colCode[0] == "R": col += 4
    if colCode[1] == "R": col += 2
    if colCode[2] == "R": col += 1
    return col

def seatID(ticket): # This calculates the seat ID, of which we need to find the highest for the answer
    row = findRow(ticket[:7])
    col = findColumn(ticket[7:])
    return 8 * row + col

ids = [seatID(ticket) for ticket in splitInput]
max_id = max(ids)
print("Part 1:")
print(max_id)

min_id = min(ids)
taken_seats = set(ids)
all_seats = set(range(min_id, max_id + 1))
print("Part 2:")
print(all_seats.difference(taken_seats))