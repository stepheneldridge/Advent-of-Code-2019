# Day 22
INPUT = open("Day 22.txt", "r")
data = []
for i in INPUT:
    if i.startswith("deal into new stack"):
        data.append(('n', 0))
    elif i.startswith("cut"):
        n = i.strip().split(" ")[-1]
        data.append(('c', int(n)))
    elif i.startswith("deal with increment"):
        n = i.strip().split(" ")[-1]
        data.append(('d', int(n)))
deck = list(range(10007))


def shuffle(deck):
    for m, c in data:
        if m == 'n':
            deck.reverse()
        elif m == 'c':
            deck = deck[c:] + deck[:c]
        elif m == 'd':
            new_deck = deck.copy()
            for i in range(len(deck)):
                new_deck[(i * c) % len(deck)] = deck[i]
            deck = new_deck
    return deck


print("part_1:", shuffle(deck).index(2019))
cards = 119315717514047
shuffles = 101741582076661
ops = [0, 1]
for m, c in data:
    if m == 'n':
        ops[0] *= -1
        ops[1] *= -1
        ops[0] += cards - 1
    elif m == 'c':
        ops[0] += cards - c
    elif m == 'd':
        ops[0] *= c
        ops[1] *= c
ops[0] %= cards
ops[1] %= cards


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    a %= m
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x


inv = modInverse(ops[1], cards)
x = 2020
b = inv * (1 - pow(inv, shuffles, cards)) * modInverse(1 - inv, cards) * ops[0]
y = (pow(inv, shuffles, cards) * x - b) % cards
print("part_2:", y)
