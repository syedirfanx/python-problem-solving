n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))
a, b = 0.0, 0
for i in range(n):
    a += x[i] * w[i]
    b += w[i]
print("%0.1f" % (a/b))
