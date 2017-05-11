#!/usr/bin/env python

import fileinput

IPv6 = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'


#Split the IP in colons

hex_groups = IPv6.split(':')
print hex_groups


#Join method to get the original IPv6

IPv6_original = ':'.join(hex_groups)
print IPv6_original

#remove trailing \n in example:

for line in fileinput.input():
    print line.replace('\n','').split(".")

