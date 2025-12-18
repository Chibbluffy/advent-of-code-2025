import math

def findDistance(a, b):
    return math.sqrt(abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2 + abs(a[2] - b[2])**2)

with open("testinput", 'r') as f:
    line = list(map(str.strip, f.read().strip().splitlines()))
    boxes = [list(map(int, list(x))) for x in [x.split(',') for x in line]]

    print(boxes)

    circuits = []

    for box in boxes:

