from binascii import unhexlify,hexlify
from base64 import b64encode, b64decode
import math

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

def score(string):
    freq = {}
    freq[' '] = 30
    freq['e'] = 29
    freq['t'] = 28
    freq['a'] = 27
    freq['o'] = 26
    freq['i'] = 25
    freq['n'] = 24
    freq['s'] = 23
    freq['h'] = 22
    freq['r'] = 21
    freq['d'] = 20
    freq['l'] = 19
    freq['u'] = 18
    freq['c'] = 17
    freq['m'] = 16
    freq['f'] = 15
    score = 0
    for c in string.lower():
    	if c in freq:
        	score += freq[c]
    return score

KEYSIZE = 0
normalized_distances = []
for key_size in range(2, 40):
    s1 = opt_string[:key_size]
    s2 = opt_string[key_size:key_size*2]
    s3 = opt_string[key_size*2:key_size*3]
    s4 = opt_string[key_size*3:key_size*4]

    normalized_distance = float(HammingDistance(s1, s2) + HammingDistance(s2, s3) + HammingDistance(s3, s4)) / (key_size * 3)
    normalized_distances.append((key_size, normalized_distance))

normalized_distances = sorted(normalized_distances, key=lambda (_, y): y)

def single_char_xor(string):
    max_score = 0
    english_plaintext = ''
    key = ''
    local_score = 0

    for i in range(256):
        plaintext = ''
        for x in range(0,len(string)):
            xor_char = chr(ord(string[x])^i)
            plaintext += xor_char
        local_score = score(plaintext)

        if local_score > max_score:
            max_score = local_score
            english_plaintext = plaintext
            key = chr(i)
    return key, english_plaintext

for key_size, _ in normalized_distances[:5]:
    number_of_blocks = math.ceil(len(opt_string)/key_size)
    blocks = []
    for size in range(0, int(number_of_blocks)):
        blocks.append(opt_string[size*key_size:(size+1)*key_size])
    keys = ''
    for key in range(key_size):
        transpose_string = ''
        for string in blocks:
            if len(string) < key+1:
                continue
            else:
                transpose_string += string[key]
                
        keys += single_char_xor(transpose_string)[0]
        
    print key_size, keys
