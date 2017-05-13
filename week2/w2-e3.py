#!/usr/bin/env python
# entry lines in file "w2-e3.txt". For executing from shell we use:
# cat w2-e3.txt | ./w2-e3.py

import fileinput

lines = []
IP_PREF_TXT = 'ip_prefix'
AS_PATH_TXT = 'as_path'
row_prefix_list = [] #list of ip-prefix strings
row_aspath_list = [] #list of as-path lists in output
row = ''
row_elements = []

print "%s %15s" % (IP_PREF_TXT, AS_PATH_TXT)

for line in fileinput.input():
    lines.append(line.strip()) # storing lines not needed
    row = lines[lines.__len__() - 1]
    row_elements = row.split(' ')
    while '' in row_elements:
        row_elements.remove('')
    row_prefix_list.append(row_elements[1])
    aspath_index = row_elements.index('701')
    row_aspath_list.append(row_elements[row_elements.index('701'):])
for i in range(row_prefix_list.__len__()):
    print "%s %15s" % (row_prefix_list[i], row_aspath_list[i])

