# Day 2
INPUT = open('Day 02.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]


def run(noun, verb):
    global odata
    data = odata.copy()
    data[1] = noun
    data[2] = verb
    p = 0
    while True:
        op = data[p]
        a = data[data[p + 1]]
        b = data[data[p + 2]]
        if op == 1:
            data[data[p + 3]] = a + b
        elif op == 2:
            data[data[p + 3]] = a * b
        elif op == 99:
            break
        else:
            print(p, "error")
            break
        p += 4
    return data[0]


def find(x):
    for i in range(100):
        for j in range(100):
            output = run(i, j)
            if output == x:
                return 100 * i + j


INPUT.close()
print("part_1:", run(12, 2))
print("part_2:", find(19690720))
