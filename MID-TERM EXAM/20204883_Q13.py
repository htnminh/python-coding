dist = sorted([int(x) for x in input().split()])
rate = sorted([int(x) for x in input().split()], reverse = True)

sum = 0
for i in range(len(dist)):
    sum += dist[i] * rate[i]

print(sum)