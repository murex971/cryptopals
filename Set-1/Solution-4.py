from binascii import unhexlify,hexlify

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

max_score = 0
english_plaintext = ''
key = ''
    
for line in open("4.txt", "r"):
    str = unhexlify(line.rstrip())

    for i in range(256):
        plaintext = ''
        for x in range(0,len(str)):
            xor_char = chr(ord(str[x])^i)
            plaintext += xor_char
        local_score = score(plaintext)

        if local_score > max_score:
            max_score = local_score
            english_plaintext = plaintext
            key = chr(i)
    
print key, english_plaintext