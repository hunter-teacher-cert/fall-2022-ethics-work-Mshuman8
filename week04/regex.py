import re


def find_date(line):

  # pattern = r'[A-Z][a-z]+' -- checks for a capital letter, followed by lower case letters until it hits a capital or a non alpha character
    pattern = r'[A-Z][a-z]+ [A-Z][a-z]+' 
    result = re.findall(pattern,line)
    #result is a list that is holding all the names that fit the pattern parameters

  #Title first name
    pattern = r'((?:Dr\.|Mr\.|Ms\.|Miss|Mr|Ms) [A-Z][a-z]+)'
    result = result + re.findall(pattern,line)

  #Title First initial Last name
    pattern = r'((?:Dr\.|Mr\.|Ms\.|Miss|Mr|Ms) [A-Z] [A-Z][a-z]+)'
    result = result + re.findall(pattern,line)

  #First initial, middle initial, last name
    pattern = r'([A-Z]\. [A-Z]\. [A-Z][a-z]+)'
    result = result + re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)

# def find_date(line):
#     pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
#     result = re.findall(pattern,line)

#     pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
#     result = result + re.findall(pattern,line)
#     return result


# f = open("names.txt")
# for line in f.readlines():
#     #print(line)
#     result = find_date(line)
#     if (len(result)>0):
#         print(result)