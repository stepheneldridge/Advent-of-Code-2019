# Day 14
import math
INPUT = open('Day 14.txt', 'r')
data = []
reactions = {}
for i in INPUT:
    data = i.split("=>")
    r = data[1].strip().split(" ")
    amount = int(r[0])
    chem = r[1].strip()
    react = []
    for j in data[0].strip().split(","):
        a = j.strip().split(" ")
        react.append((int(a[0]), a[1]))
    reactions[chem] = {"am": amount, "react": react}

start = "FUEL"
end = "ORE"


def addset(d, k, v):
    if k in d:
        d[k] += v
    else:
        d[k] = v


def rreduce(a, b):
    keys = list(a.keys())
    for i in keys:
        if i in b:
            x = min(a[i], b[i])
            a[i] -= x
            b[i] -= x
            if a[i] == 0:
                del a[i]
            if b[i] == 0:
                del b[i]


def get_reactants(left, right):
    new_left = {}
    while len(new_left) > 1 or end not in new_left:
        new_left = {}
        for i in left:
            addset(new_left, i, left[i])
            if i in reactions:
                r = reactions[i]
                mul = int(math.ceil(left[i] / r["am"]))
                addset(right, i, r["am"] * mul)
                for j in r["react"]:
                    addset(new_left, j[1], j[0] * mul)
        rreduce(new_left, right)
        left = new_left
    return new_left, right


left = {start: 1, end: 0}
right = {}
print("part_1:", get_reactants(left, right)[0][end])

fuel = 0
low = 0
high = 10000000
target = 1000000000000
answer = 0
while low < high:
    guess = (low + high) // 2
    left = {start: guess, end: 0}
    a, b = get_reactants(left, right)
    if guess == high or guess == low:
        if a[end] > target:
            answer = guess - 1
        else:
            answer = guess
        break

    if a[end] > target:
        high = guess
    elif a[end] < target:
        low = guess
    else:
        answer = guess
        break
print("part_2", answer)
