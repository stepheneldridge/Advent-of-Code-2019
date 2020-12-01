# Day 6
INPUT = open('Day 06.txt', 'r')
odata = {}
for i in INPUT:
    x = i.strip().split(')')
    if x[0] in odata:
        odata[x[0]].append(x[1])
    else:
        odata[x[0]] = [x[1]]

root = 'COM'
totals = 0
you = []
san = []
def build_tree(node, path=[], d=0):
    global odata
    global totals
    global san
    global you
    branch = {}
    if node == "SAN":
        san = path
    elif node == "YOU":
        you = path
    if node in odata:
        for i in odata[node]:
            branch[i] = build_tree(i, path=path + [node], d=d + 1)
    totals += d
    return branch

build_tree(root)
print("part_1:", totals)

for i in range(len(you)):
    if you[-(i + 1)] in san:
        print("part_2:", i + len(san) - san.index(you[-(i + 1)]) - 1)
        break

