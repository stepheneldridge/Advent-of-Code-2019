# Day 24
INPUT = open('Day 24.txt', 'r')
data = []
for i in INPUT:
    data.append(tuple(i.strip()))
INPUT.close()
datac = tuple(data.copy())
seen = []
check = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]
while datac not in seen:
    seen.append(datac)
    new_data = []
    for i in range(len(datac)):
        row = []
        for j in range(len(datac[i])):
            count = 0
            for k in check:
                x = j + k[0]
                y = i + k[1]
                if x >= 0 and x < len(datac[i]) and y >= 0 and y < len(datac):
                    if datac[y][x] == "#":
                        count += 1
            if datac[i][j] == "#":
                if count != 1:
                    row.append(".")
                else:
                    row.append("#")
            else:
                if count == 1 or count == 2:
                    row.append("#")
                else:
                    row.append(".")
        new_data.append(tuple(row))
    datac = tuple(new_data)

value = 0
for i in range(len(datac)):
    for j in range(len(datac[i])):
        if datac[i][j] == "#":
            value += 1 << (5 * i + j)
print("part_1:", value)

minutes = 200
tiles = {0: [list(i) for i in data]}
for i in range(minutes // 2 + 1):
    tiles[i + 1] = [["." for k in range(5)] for j in range(5)]
    tiles[-i - 1] = [["." for k in range(5)] for j in range(5)]
for index in range(minutes):
    new_tiles = {}
    for level in tiles:
        new_data = []
        for i in range(5):
            row = []
            for j in range(5):
                count = 0
                if i == 2 and j == 2:
                    row.append(".")
                    continue
                for k in check:
                    x = j + k[0]
                    y = i + k[1]
                    if x == 2 and y == 2 in tiles:
                        if (level + 1) not in tiles:
                            continue
                        if k[1] == 1:
                            count += [tiles[level + 1][i][0] for i in range(5)].count("#")
                        elif k[1] == -1:
                            count += [tiles[level + 1][i][4] for i in range(5)].count("#")
                        elif k[0] == 1:
                            count += [tiles[level + 1][0][i] for i in range(5)].count("#")
                        elif k[0] == -1:
                            count += [tiles[level + 1][4][i] for i in range(5)].count("#")
                    elif x >= 0 and x < 5 and y >= 0 and y < 5:
                        if tiles[level][y][x] == "#":
                            count += 1
                    elif (level - 1) in tiles:
                        t = "."
                        if x < 0:
                            t = tiles[level - 1][1][2]
                        elif x >= 5:
                            t = tiles[level - 1][3][2]
                        elif y < 0:
                            t = tiles[level - 1][2][1]
                        elif y >= 5:
                            t = tiles[level - 1][2][3]
                        if t == "#":
                            count += 1
                if tiles[level][i][j] == "#":
                    if count != 1:
                        row.append(".")
                    else:
                        row.append("#")
                else:
                    if count == 1 or count == 2:
                        row.append("#")
                    else:
                        row.append(".")
            new_data.append(row)
        new_tiles[level] = new_data
    tiles = new_tiles
count = 0
for i in tiles:
    for j in tiles[i]:
        count += j.count("#")
print("part_2:", count)
