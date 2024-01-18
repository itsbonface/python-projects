# Importing the regex module
import re

# Function to evaluate if a specific pattern matches in a given string 
# using re.search(<regex>, <string>, <flags>) object
def evaluate_match(pattern='123', string='Born on 31-12-1999. \nIs he now 25years?'):
    # Since the match object  is a boolean
    if re.subsearch(pattern, string):
        print(re.search(pattern, string))
        return 'Found a match.'
    return 'No match.'

# Metacharacters

# [] ~ Specifies a character class
pattern1 = ['Bo[qrs]n', 'Is [a-zA-Z]e', '[0-9a-fA-F]', '[^0-9a-z]']
# \d or [0-9] ~ Match based on whether a characher is a decimal digit. \D isn't.
pattern2 = r'[\d][0-9][234]'
# dot(.) ~ Specifies a wildcard
pattern3 = '1.3'
# \w or [a-zA-Z0-9_] ~ Match based on whether a character is a word character. \W isn't.
pattern4 = r'[\w]orn'
# \s ~ Match based on whether a character represents whitespace
pattern5 = r'[\s]I'
# Backslash(\) ~ Removes the special meaning of a metacharacter
pattern6 = '\\06' # or use row string
# Anchors(^ or \A) ~ Anchor a match to the start of a string
pattern7 = '^Born'
# Anchors($ or \Z) ~ Anchor a match to the end of a string
pattern8 = r'25years\?'
# Anchor(\b) ~ Anchors a match to a word boundary. \B isn't.
pattern9 = [r'\bBorn', r'\bon\b', r'1999\b', r'years[\?]\b']
# * ~ Matches zero or more repetitions of the preceeding regex
pattern10 = 'Bo-*rn.*1999.'

pattern11 = 'Born on '


print(evaluate_match(pattern9[1]))