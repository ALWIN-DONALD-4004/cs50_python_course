# docs.python.org/3/library/random.html
# random.choice(seq)

# generate of head or tail

import random

coin = random.choice(["heads","tails"])
print(coin)


from random import choice

coin = choice(["heads","tails"])
print(coin)


# random.randint(a,b) from = a, to = b

number = random.randint(1,10)
print(number)


# random.shuffle(x) 
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)