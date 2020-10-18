import sys
args = sys.argv

method = args[1]
msg = args[2]
key = args[3]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
dict = {}

count = 0
for char in alphabet:
    dict[char]=count
    count+=1

def decode(letter,key,method):
    if method == "decode":
        return alphabet[(dict[char]-dict[key])%26]
    else:
        return alphabet[(dict[char]+dict[key])%26]

charcount = 0
mod = len(key)
decoded = ""
for char in msg.lower():
    decoded += decode(msg,key[charcount%mod],method)
    charcount += 1
print(decoded)