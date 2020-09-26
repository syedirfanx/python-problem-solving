import math

def cdf(x, m, sd):
    return 0.5 * (1 + math.erf((x - m)/(sd * math.sqrt(2))))
    

max_weight = int(input().strip())
n = int(input().strip())
m = float(input().strip())
sd = float(input().strip())

clt = round(cdf(max_weight, n * m, math.sqrt(n) * sd), 4)

print("%.4f" % clt)