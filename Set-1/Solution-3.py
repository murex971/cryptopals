# (A xor B) xor B = A

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

def break_the_hack(hex_string):
    max_score = 0
    english_plaintext = ''
    key = ''
    pscore = 0

    for i in range(256):
        plaintext = ''
        for x in range(0,len(hex_string)):
            xor_char = chr(ord(hex_string[x])^i)
            plaintext += xor_char
        pscore = score(plaintext)

        if pscore > max_score:
            max_score = pscore
            english_plaintext = plaintext
            key = chr(i)
    return key, english_plaintext

str1 = unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
print break_the_hack(str1)
