import re

with open('input.txt', 'r') as f:
# with open('sampleInput.txt', 'r') as f:
    data = f.read().splitlines()

passports = []
newLine = ''
for row in data:
    if row == '':
        passports.append(newLine.strip())
        newLine = ''
        continue

    newLine += row + ' '
passports.append(newLine.strip())

validPassports = []
# Puzzle 1
validCount = 0
for passport in passports:
    # print(passport)
    if 'byr' not in passport: continue
    if 'iyr' not in passport: continue
    if 'eyr' not in passport: continue
    if 'hgt' not in passport: continue
    if 'hcl' not in passport: continue
    if 'ecl' not in passport: continue
    if 'pid' not in passport: continue
    # if 'cid' not in passport: continue
    validCount += 1
    validPassports.append(passport)

# print(len(passports))
print('Puzzle 1: ' + str(validCount))

# Puzzle 2
validCount2 = 0
for passport in validPassports:
    # if 'byr' not in passport: continue
    # if 'iyr' not in passport: continue
    # if 'eyr' not in passport: continue
    # if 'hgt' not in passport: continue
    # if 'hcl' not in passport: continue
    # if 'ecl' not in passport: continue
    # if 'pid' not in passport: continue
    
    invalid = False
    elements = passport.split()
    for el in elements:
        if invalid: break
        key, val = el.split(':')
        if key == 'byr':
            if int(val) < 1920 or int(val) > 2002:
                invalid = True
        elif key == 'iyr':
            if int(val) < 2010 or int(val) > 2020:
                invalid = True
        elif key == 'eyr':
            if int(val) < 2020 or int(val) > 2030:
                invalid = True
        elif key == 'hgt' and 'cm' in val:
            if  int(val[:-2]) < 150 or int(val[:-2]) > 193:
                invalid = True
        elif key == 'hgt' and 'in' in val:
            if  int(val[:-2]) < 59 or int(val[:-2]) > 76:
                invalid = True
        elif key == 'hcl':
            pat = '#([a-f0-9]{6})'
            if not re.match(pat, val):
                invalid = True
        elif key == 'ecl':
            if val == 'amb' or val == 'blu' or val == 'brn' or val == 'gry' or val == 'grn' or val == 'hzl' or val == 'oth':
                pass
            else:
                invalid = True
        elif key == 'pid':
            if len(val) != 9:
                invalid = True

    if not invalid: print(passport, invalid)
    if invalid: continue

    validCount2 += 1


# PROPER ANSWER IS 186 BUT RESULT IS OFF BY 1... WHY?
print('Puzzle 2: ' + str(validCount2))