# Generators - basic example #1
# Major superpower of generators is that they take up almost no RAM
# ^^This is a major advantage over lists and tuples

from itertools import islice, cycle
from string import ascii_lowercase

def count(n: int):
    i = n
    while True:
        yield i
        i += 1


counter = count(1)

for item in islice(counter, 10):
    print(item)

    
# Generators - basic example #2

from itertools import islice, cycle
from string import ascii_lowercase

def alpha():
    yield from cycle(ascii_lowercase)


for item in islice(alpha(), 26):
    print(item)

    
# Iterators = basic example #1

from itertools import islice, cycle
from string import ascii_lowercase

arr = iter(range(1,11))

for _ in range(5):
    print(next(arr))

print("stop")

for _ in range(5):
    print(next(arr))

    
    
# Another generator

!pip install IteratorAlgorithms
from random import randint
from IteratorAlgorithms import generate

d100 = generate(randint, 1, 100)
for index, roll in enumerate(d100, 1):
    print(index, roll)
    if index >= 10:
        break
