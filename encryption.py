import random
import string
chars=string.punctuation + string.ascii_letters+" "+string.digits
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)

txt=input("enter text to encrypt")
ctxt=""
for letter in txt:
    index=chars.index(letter)
    ctxt+=keys[index]
print(f" the cipher message is {ctxt}")

#decript
cctxt=input("enter value to decipher")
ttxt=""
for cc in cctxt:
    ind=chars.index(cc)
    txt+=keys[ind]
print(f"the deciphered answer is{txt}")

