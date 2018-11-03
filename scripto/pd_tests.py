from urllib.parse import urlparse, parse_qs
import pandas as pd
import os
import re
from collections import Counter

loc = './test-input/AL_PA_DIWALI_HNW_FILE_30OCT.xlsx'

df = pd.read_excel(loc)

names_list = []
char_count = []
for k in df['LONG_URL']:
    if k != '':
        parsed = urlparse(k)
        name = parse_qs(parsed.query)['tbcustname']

        if type(name[0]) != str:
            names_list.append('Empty')
            char_count.append(0)
        else:
            z = re.findall('[A-Z][^A-Z]*', name[0])
            names_list.append(z[0])
            char_count.append(len(z[0]))
    else:
        names_list.append('empty url')
        char_count.append(0)

print(len(df['LONG_URL']))
print(len(names_list))
print(len(char_count))
print(Counter(char_count))