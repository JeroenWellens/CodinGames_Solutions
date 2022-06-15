maximum = 0
loss = []
with open('source.txt') as f:

    n = int(f.readline())
    for i in f.readline().split():
        v = int(i)
        if v > maximum:
            maximum = v
            minimum = v
        if v < minimum:
            minimum = v
        loss.append(minimum-maximum)
print(min(loss))