# A. Prompts the user to enter an IP network (/24)

IPv4_net_str = raw_input("Please enter a /24 network:\n")


# B. Stores the IP network as a list of octets strings

IPv4_net_octets = IPv4_net_str.split(".")

#if last element is [], it is removed
first_length = len(IPv4_net_octets)
if IPv4_net_octets[first_length-1] == '':
    IPv4_net_octets.pop()
    
length = len(IPv4_net_octets)

if ( length < 3 ) | (length > 4):
    print "The IP network is no valid"
elif (length == 4) & (IPv4_net_octets[length-1] != '0'):
    print "The last octet is not zero"
else:
    
    if length == 3:
        IPv4_net_octets.append("0")
    
# C. Prints the network out to the screen
    IPv4_net_str_4octets = '.'.join(IPv4_net_octets)
    print "The IP network is: %s" % IPv4_net_str_4octets
    
    
# D. Print a table with first octet of network in binary and hexadecimal
    
    IPv4_firstoctet_bin = bin(int(IPv4_net_octets[0]))
    IPv4_firstoctet_hex = hex(int(IPv4_net_octets[0]))
    
    NET_NUM_TXT = 'NETWORK_NUMBER'
    FIRST_BIN_TXT = 'FIRST_OCTET_BINARY'
    FIRST_HEX_TXT = 'FIRST_OCTET_HEX'
    
    print "%s %20s %20s" % (NET_NUM_TXT, FIRST_BIN_TXT, FIRST_HEX_TXT)
    print "%s %20s %20s" % (IPv4_net_str_4octets, IPv4_firstoctet_bin, IPv4_firstoctet_hex)


