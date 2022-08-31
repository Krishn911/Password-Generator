import random 
import string

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

passlen = int(input("Enter Length: "))

s = []

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)

newpass = ("".join(s[0:passlen]))
print(newpass)
