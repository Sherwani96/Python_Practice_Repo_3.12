import re

regex = r"([a-zA-Z]).([a])"    # r here stands for raw string, it used here to ignore any special character like \ /

val = 'search this inside of this text please!!'

# here are two groups of regex we are searching for in the above sentence
# using . in regex makes groups of regex
matches = re.search(regex, val)
print(matches.groups())
print(matches)