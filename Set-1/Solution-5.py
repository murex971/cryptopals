from binascii import unhexlify,hexlify

def repeatedXOR(str, key):
    key_length = len(key)
    output = ""
    for x in range(0,len(str)):
        output+= (chr(ord(str[x])^ord(key[x%key_length])))
    print hexlify(output)
