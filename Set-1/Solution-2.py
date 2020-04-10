from binascii import unhexlify,hexlify

def XORfunc(str1, str2):
    a = unhexlify(str1)
    b = unhexlify(str2)
    output = ""
    for x in range(0,len(a)):
        output+= (chr(ord(a[x])^ord(b[x])))
    print hexlify(output)