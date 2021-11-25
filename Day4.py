from get_aoc import get_input

rawInput = get_input(4)

splitInput = rawInput.split("\n\n") # Splitting the data into a list

# Converts a passport specification string into a dictionary.
#
# Example:
#   parse_passport('hgt:150cm pid:660176034 hcl:#c0946f')
#   => {'hgt': '150cm', 'pid': '660176034', 'hcl': '#c0946f'}
def parse_passport(raw):
    fields = raw.split()

    passport = dict()
    for field in fields:
        key, value = field.split(':')
        passport[key] = value

    return passport

passports = [parse_passport(line) for line in splitInput]

# For part 1, a passport is valid if it has 7 fields, not including cid
def valid_passport(passport):
    return sum(field != 'cid' for field in passport.keys()) == 7

valid_passports = [pp for pp in passports if valid_passport(pp)]
numCorrectPP = len(valid_passports)

print(numCorrectPP)
