s="HaCkEr"
new_s=""
for letter in s:
    if letter.isupper():
        new_s+=letter.lower()
    else:
        new_s+=letter.upper()
print(new_s)

import array as arr
arr=[1,2,3,4,5]
a=arr[::-1]
print(a)

#LAMBDA

a=lambda x,y:x+y
print(a(5,6))


#randomized items of list
from random import shuffle
x = ['hackr.io', 'Is', 'The', 'Best', 'For', 'Learning', 'Python']
shuffle(x)
print(x)

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
print(Counter(d1))
new_dict = Counter(d1) + Counter(d2)
print(new_dict)


