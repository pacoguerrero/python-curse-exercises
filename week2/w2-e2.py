# A. Prompts the user to enter an IP address

IPv4_str = raw_input("Please enter an IP version 4:\n")


# B. Converts dotted decimal IPv4 to binary string

IPv4_octets = IPv4_str.split(".")
    
length = len(IPv4_octets)

if ( length != 4):
    print "The IP network is not valid"
elif (length == 4) & (IPv4_octets[length-1] == ''):
    print "The IP address is not valid"
else:
    #there is no values validation check
    firstoctet_bin = bin(int(IPv4_octets[0]))
    secondoctet_bin = bin(int(IPv4_octets[1]))
    thirdoctet_bin = bin(int(IPv4_octets[2]))
    forthoctet_bin = bin(int(IPv4_octets[3]))
    
    FIRST_OCTET_TXT = 'first_octet'
    SECOND_OCTET_TXT = 'second_octet'
    THIRD_OCTET_TXT = 'third_octet'
    FORTH_OCTET_TXT = 'forth_octet'
    
    print "%s %15s %15s %15s" % (FIRST_OCTET_TXT, SECOND_OCTET_TXT, THIRD_OCTET_TXT, FORTH_OCTET_TXT)
    print "%s %15s %15s %15s" % (firstoctet_bin, secondoctet_bin, thirdoctet_bin, forthoctet_bin)


