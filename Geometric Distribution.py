num, den = map(float, input().split())
n = int(input())
p = num / den
q = 1 - p
gd = (q**(n - 1))*p
print(round(gd, 3))
