# Day 5
INPUT = open('Day 05.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]


def run(code):
    global odata
    data = odata.copy()
    p = 0
    outputs = []
    while True:
        op = data[p] % 100
        am = (data[p] // 100) % 10
        bm = (data[p] // 1000) % 10
        # cm = (data[p] // 10000) % 10

        if op == 1:
            a = data[data[p + 1]] if am == 0 else data[p + 1]
            b = data[data[p + 2]] if bm == 0 else data[p + 2]
            data[data[p + 3]] = a + b
            p += 4
        elif op == 2:
            a = data[data[p + 1]] if am == 0 else data[p + 1]
            b = data[data[p + 2]] if bm == 0 else data[p + 2]
            data[data[p + 3]] = a * b
            p += 4
        elif op == 3:
            data[data[p + 1]] = code
            p += 2
        elif op == 4:
            a = data[data[p + 1]] if am == 0 else data[p + 1]
            outputs.append(a)
            p += 2
        elif op == 5:
            a = data[data[p + 1]] if am == 0 else data[p + 1]
            b = data[data[p + 2]] if bm == 0 else data[p + 2]
            if a != 0:
                p = b
            else:
                p += 3
        elif op == 6:
            a = data[data[p + 1]] if am == 0 else data[p + 1]
            b = data[data[p + 2]] if bm == 0 else data[p + 2]
            if a == 0:
                p = b
            else:
                p += 3
        elif op == 7:
            a = data[data[p + 1]] if am == 0 else data[p + 1]
            b = data[data[p + 2]] if bm == 0 else data[p + 2]
            data[data[p + 3]] = int(a < b)
            p += 4
        elif op == 8:
            a = data[data[p + 1]] if am == 0 else data[p + 1]
            b = data[data[p + 2]] if bm == 0 else data[p + 2]
            data[data[p + 3]] = int(a == b)
            p += 4
        elif op == 99:
            p += 1
            break
        else:
            print(p, "error")
            break
    assert not any(outputs[:-1])
    return outputs[-1]


INPUT.close()
print("part_1:", run(1))
print("part_2:", run(5))
