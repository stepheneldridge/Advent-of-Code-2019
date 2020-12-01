# Day 12
import math
moons = [
    [-17, 9, -5],
    [-1, 7, 13],
    [-19, 12, 5],
    [-6, -6, -4]
]
moons2 = [
    [-17, 9, -5],
    [-1, 7, 13],
    [-19, 12, 5],
    [-6, -6, -4]
]

vel = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(1000):
    for j in range(len(moons)):
        for k in range(len(moons) - j - 1):
            n = k + j + 1
            for v in range(len(moons[j])):
                if moons[j][v] < moons[n][v]:
                    vel[j][v] += 1
                    vel[n][v] -= 1
                elif moons[j][v] > moons[n][v]:
                    vel[j][v] -= 1
                    vel[n][v] += 1
    for m in range(len(moons)):
        for v in range(len(moons[m])):
            moons[m][v] += vel[m][v]


def abssum(x, y):
    s = 0
    for i in range(len(x)):
        s += sum([abs(a) for a in x[i]]) * sum([abs(b) for b in y[i]])
    return s


print("part_1:", abssum(moons, vel))


def find_r(moons, v):
    past = []
    c = [i[v] for i in moons] + [0, 0, 0, 0]
    count = 0
    while c not in past:
        count += 1
        if len(past) == 0:
            past.append(c.copy())
        for j in range(4):
            for k in range(4 - j - 1):
                n = k + j + 1
                if c[j] < c[n]:
                    c[4 + j] += 1
                    c[4 + n] -= 1
                elif c[j] > c[n]:
                    c[4 + j] -= 1
                    c[4 + n] += 1
        for m in range(4):
            c[m] += c[4 + m]
    return count


a = find_r(moons2, 0)
b = find_r(moons2, 1)
c = find_r(moons2, 2)
a = a * b // math.gcd(a, b)
a = a * c // math.gcd(a, c)
print("part_2:", a)
