# Day 8

[Puzzle](https://adventofcode.com/2025/day/8)

[Puzzle Input](./input)

[Part 1 puzzle answer](#part-1-puzzle-answer)

[Part 2 puzzle answer](#part-2-puzzle-answer)

## Part 1 Work

This puzzle reminds me of graphs and edges/vertices in my CS Data Structures and Algorithms class.
I start out calculating the distances between each point. No need to duplicate the points though, so we make the `for` loop this:
```python
  for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
```
After finding the distances, we sort them and process them one by one.

I was misled by the instructions:
"The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!"
I thought that this meant there is no connection added, so it does not count. But it in fact does count. I was making it too efficient by trying to not use a cable to connect it to save on cables since it was already connected. 

The logic from here is just updating the circuits when a connection is made, not too difficult. 

```python
import math

def findDistance(a, b):
    return math.sqrt(
        abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2 + abs(a[2] - b[2]) ** 2
    )

def isInCircuit(box, circuit):
    box = tuple(box)
    for b in circuit:
        if box == b:
            return True
    return False

def product(lst):
    result = 1
    for x in lst:
        result *= x
    return result

with open("input", "r") as f:
    line = list(map(str.strip, f.read().strip().splitlines()))
    boxes = [tuple(map(int, list(x))) for x in [x.split(",") for x in line]]
    unconnected_boxes = boxes.copy()
    connections = []
    circuits = []
    distances = []

    # Calculate all distances and sort
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = findDistance(boxes[i], boxes[j])
            distances.append((boxes[i], boxes[j], dist))
    distances.sort(key=lambda x: x[2])

    # Process distances
    count = 0
    stop_after = 1000
    for d in distances:
        count += 1
        box_a, box_b, dist = d

        # Completely new connection
        if box_a in unconnected_boxes and box_b in unconnected_boxes:
            connections.append((box_a, box_b, dist))
            circuits.append(set((box_a, box_b)))
            unconnected_boxes.remove(box_a)
            unconnected_boxes.remove(box_b)
        # One box is already connected
        elif box_a in unconnected_boxes or box_b in unconnected_boxes:
            connections.append((box_a, box_b, dist))
            for circuit in circuits:
                if isInCircuit(box_a, circuit) or isInCircuit(box_b, circuit):
                    if isInCircuit(box_a, circuit):
                        unconnected_boxes.remove(box_b)
                    else:
                        unconnected_boxes.remove(box_a)
                    circuit.add(box_a)
                    circuit.add(box_b)
                    break

        # Both boxes are already connected
        else:
            circuit_a = None
            circuit_b = None
            for circuit in circuits:
                if isInCircuit(box_a, circuit):
                    circuit_a = circuit
                if isInCircuit(box_b, circuit):
                    circuit_b = circuit
                if circuit_a is not None and circuit_b is not None:
                    break
            # Merge circuits if they are different
            if circuit_a != circuit_b:
                connections.append((box_a, box_b, dist))
                circuit_a.update(circuit_b)
                circuits.remove(circuit_b)

        if count >= stop_after:
            break

    lengths = []
    for circuit in circuits:
        lengths.append(len(circuit))
    # print("Circuit lengths:", lengths)
    lengths.sort()
    # print(lengths[-3:])
    print(product(lengths[-3:]))

```

## Part 2 Work

Suuuper small change to get part 2. Remove the 1000 limit and add a check for when there are no more disconnected boxes and only one circuit. The pair it stops on is the one we are looking for!

```python
import math


def findDistance(a, b):
    return math.sqrt(
        abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2 + abs(a[2] - b[2]) ** 2
    )


def isInCircuit(box, circuit):
    box = tuple(box)
    for b in circuit:
        if box == b:
            return True
    return False


def product(lst):
    result = 1
    for x in lst:
        result *= x
    return result


with open("testinput", "r") as f:
    line = list(map(str.strip, f.read().strip().splitlines()))
    boxes = [tuple(map(int, list(x))) for x in [x.split(",") for x in line]]
    unconnected_boxes = boxes.copy()
    connections = []
    circuits = []
    distances = []

    # Calculate all distances and sort
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = findDistance(boxes[i], boxes[j])
            distances.append((boxes[i], boxes[j], dist))
    distances.sort(key=lambda x: x[2])

    # Process distances
    for d in distances:
        box_a, box_b, dist = d

        # Completely new connection
        if box_a in unconnected_boxes and box_b in unconnected_boxes:
            # print("New circuit")
            connections.append((box_a, box_b, dist))
            circuits.append(set((box_a, box_b)))
            unconnected_boxes.remove(box_a)
            unconnected_boxes.remove(box_b)
        # One box is already connected
        elif box_a in unconnected_boxes or box_b in unconnected_boxes:
            connections.append((box_a, box_b, dist))
            for circuit in circuits:
                if isInCircuit(box_a, circuit) or isInCircuit(box_b, circuit):
                    if isInCircuit(box_a, circuit):
                        unconnected_boxes.remove(box_b)
                    else:
                        unconnected_boxes.remove(box_a)
                    circuit.add(box_a)
                    circuit.add(box_b)
                    break
        # Both boxes are already connected
        else:
            circuit_a = None
            circuit_b = None
            for circuit in circuits:
                if isInCircuit(box_a, circuit):
                    circuit_a = circuit
                if isInCircuit(box_b, circuit):
                    circuit_b = circuit
                if circuit_a is not None and circuit_b is not None:
                    break
            # Merge circuits if they are different
            if circuit_a != circuit_b:
                connections.append((box_a, box_b, dist))
                circuit_a.update(circuit_b)
                circuits.remove(circuit_b)

        if len(unconnected_boxes) == 0 and len(circuits) == 1:
            print(d)
            print(box_a[0] * box_b[0])
            break

```


##### Part 1 puzzle answer 

Your puzzle answer was 96672.

##### Part 2 puzzle answer 

Your puzzle answer was 22517595.
