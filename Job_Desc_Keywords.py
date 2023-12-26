import os
import re
import csv
"""
Open each file in the job desc folder
Strip punctuation and use casefold on every word
count frequency of words
Ignore common words like a, the, he, etc
"""
# TODO change to accept input for path
path = # path
common_words = ["a", "the", "if", "for", "and", "to", "of", "in", "with", "test", "we",
                "experience", "or", "you", "testing", "our", "is", "are", "software",
                "as", "team", "on", "quality", "work", "that", "will", "be", "qa", "an",
                "this", "your", "s", "at", "job", "all", "remote", "by", "have", "skills",
                "engineer", "tools", "other", "", "product", "from", "years", "requirements",
                "working", "company", "assurance", "about", "years", "including", "us", "status",
                "role", "knowledge", "time", "it", "teams", "ability", "new", "strong", "more",
                "business", "not", "any", "benefits", "who", "what", "cases", "plans", "process",
                ]
desc_dict = {}

for file in os.listdir(path):
    # easier to ignore char errors than strip out any offending ones
    open_file = open(os.path.join(path, file), "r", encoding='utf-8', errors='ignore')
    # print(file)
    for line in open_file:
        # remove punctuation and make all lowercase
        fixed_line = (re.sub("[,.!?@%()’&`~$*^_=<>:\[\]/\'\"–●—•]", " ", line)).casefold()
        for word in fixed_line.split():
            # ignore many words that aren't useful
            if word in common_words:
                pass
            # add new words to dictionary, initialize value to 1
            elif word not in desc_dict:
                desc_dict[word] = 1
            # if word exists in dictionary, increase count by 1
            else:
                desc_dict[word] += 1
    # close file after loop
    open_file.close()

with open('newfile.csv', 'w', encoding='utf-8') as newfile:
    for k, v in desc_dict.items():
        # ignore anything repeated only a few times
        if v < 100:
            pass
        else:
            newfile.write(str(k) + ',' + str(v) + '\n')
newfile.close()
