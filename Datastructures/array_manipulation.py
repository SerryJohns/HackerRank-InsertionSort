n, inputs = [int(n) for n in input().split(' ')]
ls = [0] * (n + 1)

for _ in range(inputs):
    x, y, value = [int(n) for n in input().split(' ')]
    ls[x - 1] += value
    if y <= len(ls):
        ls[y] -= value

max_val = x = 0
for i in ls:
    x = x + i
    if max_val < x:
        max_val = x

print(max_val)
