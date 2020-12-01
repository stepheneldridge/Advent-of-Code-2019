# Day 7
from itertools import permutations as perm
INPUT = open('Day 07.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]


def run(phases):
    pid = 0
    data = [odata.copy() for i in phases]
    p = [0 for i in phases]
    outputs = [[i] for i in phases]
    outputs[0].append(0)
    while True:
        op = data[pid][p[pid]] % 100
        am = (data[pid][p[pid]] // 100) % 10
        bm = (data[pid][p[pid]] // 1000) % 10

        if op == 1:
            a = data[pid][data[pid][p[pid] + 1]] if am == 0 else data[pid][p[pid] + 1]
            b = data[pid][data[pid][p[pid] + 2]] if bm == 0 else data[pid][p[pid] + 2]
            data[pid][data[pid][p[pid] + 3]] = a + b
            p[pid] += 4
        elif op == 2:
            a = data[pid][data[pid][p[pid] + 1]] if am == 0 else data[pid][p[pid] + 1]
            b = data[pid][data[pid][p[pid] + 2]] if bm == 0 else data[pid][p[pid] + 2]
            data[pid][data[pid][p[pid] + 3]] = a * b
            p[pid] += 4
        elif op == 3:
            if len(outputs[pid]) == 0:
                pid = (pid + 1) % len(phases)
            else:
                data[pid][data[pid][p[pid] + 1]] = outputs[pid].pop(0)
                p[pid] += 2
        elif op == 4:
            a = data[pid][data[pid][p[pid] + 1]] if am == 0 else data[pid][p[pid] + 1]
            outputs[(pid + 1) % len(phases)].append(a)
            p[pid] += 2
        elif op == 5:
            a = data[pid][data[pid][p[pid] + 1]] if am == 0 else data[pid][p[pid] + 1]
            b = data[pid][data[pid][p[pid] + 2]] if bm == 0 else data[pid][p[pid] + 2]
            if a != 0:
                p[pid] = b
            else:
                p[pid] += 3
        elif op == 6:
            a = data[pid][data[pid][p[pid] + 1]] if am == 0 else data[pid][p[pid] + 1]
            b = data[pid][data[pid][p[pid] + 2]] if bm == 0 else data[pid][p[pid] + 2]
            if a == 0:
                p[pid] = b
            else:
                p[pid] += 3
        elif op == 7:
            a = data[pid][data[pid][p[pid] + 1]] if am == 0 else data[pid][p[pid] + 1]
            b = data[pid][data[pid][p[pid] + 2]] if bm == 0 else data[pid][p[pid] + 2]
            data[pid][data[pid][p[pid] + 3]] = int(a < b)
            p[pid] += 4
        elif op == 8:
            a = data[pid][data[pid][p[pid] + 1]] if am == 0 else data[pid][p[pid] + 1]
            b = data[pid][data[pid][p[pid] + 2]] if bm == 0 else data[pid][p[pid] + 2]
            data[pid][data[pid][p[pid] + 3]] = int(a == b)
            p[pid] += 4
        elif op == 99:
            p[pid] += 1
            if pid < len(phases) - 1:
                pid += 1
            else:
                break
        else:
            print(p, "error")
            break
    return outputs[0][-1]


INPUT.close()
best = 0
for i in perm(range(5)):
    out = run(i)
    if out > best:
        best = out

print("part_1:", best)
best = 0
for i in perm(range(5, 10)):
    out = run(i)
    if out > best:
        best = out
print("part_2:", best)
