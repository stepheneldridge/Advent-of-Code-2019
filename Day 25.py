# Day 25
INPUT = open("Day 25.txt", "r")
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]

odata += [0 for _ in range(2000)]
p = 0
rbase = 0


def run(codes):
    global p
    global rbase
    global odata
    data = odata
    outputs = []
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
            if len(codes) > 0:
                data[data[p + 1] + (0 if am != 2 else rbase)] = codes.pop(0)
            else:
                break
            p += 2
        elif op == 4:
            a = data[data[p + 1]] if am == 0 else data[p + 1] if am == 1 else data[data[p + 1] + rbase]
            outputs.append(a)
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
            p += 1
            break
        else:
            print(p, "error")
            break
    return outputs


INPUT.close()
dirs = ["north", "south", "east", "west"]
out = run([])
items = {
    "bowl of rice": ["south", "west", "take", "east", "north"],
    "astronaut ice cream": ["south", "east", "east", "take", "west", "west", "north"],
    "": []
}
how_to_win = """
south
east
take mutex
east
take astronaut ice cream
south
take tambourine
north
west
south
south
west
south
take easter egg
west
west
"""
how_to_win = list(map(ord, how_to_win))
out = run(how_to_win)
print("".join(map(chr, out)))
# while True:
#     print("".join(map(chr, out)))
#     typed = input()
#     d = list(map(ord, typed)) + [10]
#     out = run(d)
#     text = "".join(map(chr, out))
#     doors = [True if (i in text) else False for i in dirs]
#     print(doors)
# win: easter egg, tambourine, astronaut ice cream, mutex
