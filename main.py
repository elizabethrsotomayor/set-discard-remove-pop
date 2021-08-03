n = int(input())
s = set(map(int, input().split()))
num = input()

for i in range(0, int(num)):
    cmd = input()
    if cmd == "pop":
        s.pop()
    else:
        g = cmd.split()
        if g[0] == "remove":
            s.remove(int(g[1]))
        elif g[0] == "discard":
            s.discard(int(g[1]))

sum = 0

for j in s:
    sum += j

print(sum)
