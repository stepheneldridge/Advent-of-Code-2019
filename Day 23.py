# Day 23
data = []
INPUT = open('Day 23.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]
odata += [0 for _ in range(2000)]
ps = [0 for i in range(50)]
rbases = [0 for i in range(50)]
datas = [odata.copy() for i in range(50)]
nat = [False for i in range(50)]


def run(pid, code):
    global ps
    global rbases
    global datas
    global nat
    p = ps[pid]
    rbase = rbases[pid]
    data = datas[pid]
    outputs = None
    while True:
        op = data[p] % 100
        am = (data[p] // 100) % 10
        bm = (data[p] // 1000) % 10
        cm = (data[p] // 10000) % 10
        if op == 1:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if cm == 2:
                data[data[p + 3] + rbase] = a + b
            else:
                data[data[p + 3]] = a + b
            p += 4
        elif op == 2:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if cm == 2:
                data[data[p + 3] + rbase] = a * b
            else:
                data[data[p + 3]] = a * b
            p += 4
        elif op == 3:
            if len(code) > 0:
                data[data[p + 1] + (0 if am != 2 else rbase)] = code.pop(0)
            else:
                data[data[p + 1] + (0 if am != 2 else rbase)] = -1
                nat[pid] = True
            p += 2
        elif op == 4:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            outputs = a
            nat[pid] = False
            p += 2
        elif op == 5:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if a != 0:
                p = b
            else:
                p += 3
        elif op == 6:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            if a == 0:
                p = b
            else:
                p += 3
        elif op == 7:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            data[data[p + 3] + (rbase if cm == 2 else 0)] = int(a < b)
            p += 4
        elif op == 8:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            b = data[data[p + 2]] if bm == 0 else data[p + 2] if bm == 1 else data[data[p + 2] + rbase]
            data[data[p + 3] + (rbase if cm == 2 else 0)] = int(a == b)
            p += 4
        elif op == 9:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            rbase += a
            p += 2
        elif op == 99:
            break
        else:
            print(p, "error")
            break
        break
    ps[pid] = p
    rbases[pid] = rbase
    return outputs


INPUT.close()
queue = [[i] for i in range(50)]
prequeue = [[] for i in range(50)]
last = []
sent = None
p1 = False
while True:
    for i in range(50):
        out = run(i, queue[i])
        if out is not None:
            prequeue[i].append(out)
        if len(prequeue[i]) == 3:
            dest = prequeue[i][0]
            if dest == 255:
                if not p1:
                    print("part_1", prequeue[i][2])
                    p1 = True
                last = prequeue[i][1:]
            else:
                queue[dest].extend(prequeue[i][1:])
            prequeue[i] = []
    if all(nat):
        skip = False
        for i in queue:
            if len(i) > 0:
                skip = True
        for i in prequeue:
            if len(i) > 0:
                skip = True
        if skip:
            continue
        queue[0] = last
        if len(last) > 0:
            if last[1] == sent:
                print("part_2:", sent)
                break
            sent = last[1]
