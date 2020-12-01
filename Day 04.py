# Day 4
low = "240298"
high = "784956"
count1 = 0
count2 = 0
x = low

def find_next(a):
    n = ""
    last = "0"
    fill = False
    for i in a:
        if i < last:
            fill = True
        elif not fill:
            last = i
        n += last
    return n


while x <= high:
    state = 0
    last = "0"
    for d in x:
        if d < last:
            state = -1
            x = find_next(x)
            break
        if state == 0:
            state = 1
        elif state == 1:
            if d == last:
                state = 2
        elif state == 2:
            if d == last:
                state = 4
            else:
                state = 3
        elif state == 4:
            if d != last:
                state = 5
        elif state == 5:
            if d == last:
                state = 2
        last = d
    count1 += state == 5 or state == 4
    count2 += state == 3 or state == 2
    if state != -1:
        x = str(int(x) + 1)
print("part_1:", count1 + count2)
print("part_2:", count2)
