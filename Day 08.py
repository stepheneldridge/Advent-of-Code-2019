# Day 08
data = []
rows = 25
columns = 6
layersize = rows * columns
with open('Day 08.txt', 'r') as f:
    INPUT = f.readlines()[0].strip()
    for i in range(len(INPUT) // layersize):
        layer = []
        for j in range(columns):
            layer.append(INPUT[i * layersize + j * rows: i * layersize + j * rows + rows])
        data.append(layer)
fewest = 1 << 32
index = 0
for i in range(len(data)):
    count = 0
    for row in data[i]:
        count += row.count('0')
    if count < fewest:
        fewest = count
        index = i

ones = 0
twos = 0
for row in data[index]:
    ones += row.count('1')
    twos += row.count('2')
print("part_1:", ones * twos)

result = []
for i in range(columns):
    row = []
    for j in range(rows):
        for k in range(len(data)):
            if data[k][i][j] != '2':
                row.append(data[k][i][j])
                break
    result.append(row)
print("part_2:")
for row in result:
    print("".join(row).replace("0", " ").replace("1", "#"))

