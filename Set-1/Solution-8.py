from binascii import unhexlify
from collections import defaultdict

opt_string = open("8.txt").read().splitlines()

max_repetitions = 0
result = ''
for line in opt_string:
    cipher_text = unhexlify(line)
    blocks = [cipher_text[i:i+16] for i in range(0, len(cipher_text), 16)]
    local_rep = len(blocks) - len(set(blocks))
    if local_rep > max_repetitions:
        max_repetitions = local_rep
        result = line
        
print result
