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

print("Part 1:")
print(numCorrectPP)

needs = """byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
def valid_passport2(passport):
    #print(passport.get("byr"))
    if (int(passport.get("byr")) in range(1920, 2002) and int(passport.get("iyr")) in range(2010, 2020) and (len(passport.get("hcl")) == 7 and passport.get("hcl")[0] == "#")): #this covers byr, iyr and hcl
        if ("cm" in passport.get("hgt") and int(passport.get("hgt")[:2]) in range(150, 193)) or ("in" in passport.get("hgt") and int(passport.get("hgt")[:2]) in range(59, 76)): #treats height
            available_colours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} # I chose a 'set'. Not sure if it's the best
            if passport.get("ecl") in available_colours: # Simple check if content is in set
                #print(passport)
                if len(passport.get("pid")) == 9 and passport.get("pid").isnumeric():
                    print(passport)
                    return True
        #print("true")
        #print(passport)
        #return True
    else:
        #print("false")
        return False

valid_passports2 = [pp for pp in valid_passports if valid_passport2(pp)]
numCorrectPP2 = len(valid_passports2)

print("Part 2:")
print(numCorrectPP2)

