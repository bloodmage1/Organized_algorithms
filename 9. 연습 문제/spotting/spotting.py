from math import sqrt

# case2

k = 1
d = 5
result = 26

x = range(1, d//k+1)
y = range(1, d//k+1)

answer = 1 + 2*(d//k)

for i in x:
    for j in y:
        if d >= sqrt((k*i)**2 + (k*j)**2):
            answer += 1

print(answer)

# 방법 2

d_squared = d**2
k_squared = k**2
limit = range(1, d//k+1)
answer = 1 + 2 * (d // k)

for i in limit:
    for j in limit:
        if d_squared >= (i**2 + j**2) * k_squared:
            answer += 1

print(answer)

# 방법 3

d_squared = d**2
limit = range(0, d+1, k)
answer = 0

for i in limit:
    y_spot = int(sqrt(d_squared - i**2))
    answer += y_spot//k + 1

print(answer)