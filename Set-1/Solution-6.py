from binascii import unhexlify,hexlify

def XORfunc(a, b):
    output = ""
    for x in range(0,len(a)):
        output+= (chr(ord(a[x])^ord(b[x])))
    return output

def HammingDistance(str1, str2):
    result_string = ''.join(format(ord(i), 'b') for i in XORfunc(str1, str2))
    return result_string.count("1")

print HammingDistance("this is a test", "wokka wokka!!!")