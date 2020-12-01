# Day 13
import os, time
INPUT = open('Day 13.txt', 'r')
odata = []
for i in INPUT:
    odata = [int(j) for j in i.split(",")]

odata += [0 for _ in range(2000)]

rbase = 0
p = 0
outputs = []
data = odata.copy()


def run(code):
    global data
    global p
    global rbase
    global outputs
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
            if code is not None:
                data[data[p + 1] + (0 if am != 2 else rbase)] = code
                p += 2
                code = None
            else:
                break
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
            break
        else:
            print(p, "error")
            break
    return outputs


INPUT.close()
render = run(0)
blocks = 0
small = [0, 0]
big = [0, 0]
paddlex = 0
ballx = 0
for i in range(len(render) // 3):
    x = render[3 * i]
    y = render[3 * i + 1]
    tile = render[3 * i + 2]
    if x < small[0]:
        small[0] = x
    if x > big[0]:
        big[0] = x
    if y < small[1]:
        small[1] = y
    if y > big[1]:
        big[1] = y
    if tile == 2:
        blocks += 1
    elif tile == 4:
        ballx = x
    elif tile == 3:
        paddlex = x
data = odata.copy()
data[0] = 2
screen = [
    [" " for i in range(big[0] - small[0] + 1)] for j in range(big[1] - small[1] + 1)
]


def printscreen(screen, score):
    os.system('cls')
    for i in screen:
        print("".join(i), end="\n")
    print("score:", score)
    print()
    time.sleep(0.016)


lastballx = ballx
score = 0
bally = 0


def dorender(render, screen):
    global ballx, lastballx, score, paddlex, bally
    for i in range(len(render) // 3):
        x = render[3 * i]
        y = render[3 * i + 1]
        tile = render[3 * i + 2]
        if x == -1 and y == 0:
            score = tile
        else:
            screen[y - small[1]][x - small[0]] = tiles[tile]
        if tile == 4:
            lastballx = ballx
            ballx = x
            bally = y
        elif tile == 3:
            paddlex = x


tiles = {
    0: " ",
    1: "\u2588",
    2: "\u25AA",
    3: "\u2501",
    4: "\u20DD"
}

print("part_1:", blocks)
press = 0
p = 0
rbase = 0
outputs = []
balldir = 0
bx = balldir
render = [0]
while len(render) != 0:
    render = run(press)
    dorender(render, screen)
    # printscreen(screen, score)
    balldir = ballx - lastballx
    if paddlex < ballx + balldir:
        press = 1
    elif paddlex > ballx + balldir:
        press = -1
    else:
        press = 0
    if bally == 21 and ballx == paddlex:
        press = 0
    outputs = []
print("part_2:", score)
