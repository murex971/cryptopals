from binascii import unhexlify,hexlify
from base64 import b64encode, b64decode

def XORfunc(a, b):
    output = ""
    for x in range(0,len(a)):
        output+= (chr(ord(a[x])^ord(b[x])))
    return output

def HammingDistance(str1, str2):
    # conversion to binary form.
    result_string = ''.join(format(ord(i), 'b') for i in XORfunc(str1, str2))
    return result_string.count("1")

opt_string = b64decode(''.join(open("6.txt", "r")))

normalized_distances = []
for key_size in range(2, 40):
    s1 = opt_string[:key_size]
    s2 = opt_string[key_size:key_size*2]
    s3 = opt_string[key_size*2:key_size*3]
    s4 = opt_string[key_size*3:key_size*4]

    normalized_distance = float(HammingDistance(s1, s2) + HammingDistance(s2, s3) + HammingDistance(s3, s4)) / (key_size * 3)
    normalized_distances.append((key_size, normalized_distance))

normalized_distances = sorted(normalized_distances, key=lambda (_, y): y)

print normalized_distances[0][0]