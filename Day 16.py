# Day 16
import numpy as np
INPUT = open('Day 16.txt', 'r')
data = []
for i in INPUT:
    for j in i.strip():
        data.append(int(j))
inputs = np.array(data)
for w in range(100):
    a = []
    for i in range(len(inputs)):
        p = i + 1
        phase = [0] * p + [1] * p + [0] * p + [-1] * p
        repeat = len(inputs) // len(phase) + 1
        whole = np.array((phase * repeat)[1:len(inputs) + 1])
        dot = np.dot(inputs, whole)
        a.append(abs(dot) % 10)
    inputs = np.array(a)
answer = "".join(list(map(str, inputs[0:8])))
print("part_1:", answer)

inputs = np.array(data * 10000)
offset = int("".join(list(map(str, inputs[0:7]))))
for k in range(100):
    for i in range(len(inputs) - offset):
        j = len(inputs) - i - 2
        inputs[j] = (inputs[j] + inputs[j + 1])
        if inputs[j] > 9:
            inputs[j] -= 10
answer = "".join(list(map(str, inputs[offset:offset + 8])))
print("part_2:", answer)
