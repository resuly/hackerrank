# n = int(input())
# data = [int(temp) for temp in input().split()]
n = 5
data = [1, 2, 3, 4, 5]

def check_left(j, limit):
    available = 0
    while j >= 0:
        if data[j] >= limit:
            available += 1
            j -= 1
        else:
            break
    return available

def check_right(j, limit):
    available = 0
    while j < n:
        if data[j] >= limit:
            available += 1
            j += 1
        else:
            break
    return available

stack = []
for i in range(n):
    x = data[i]
    if i == 0:
        available = check_right(i, x)
    elif i == n - 1:
        available = check_left(i, x)
    else:
        available = check_left(i-1, x) + check_right(i, x)
    # print(x, available)
    area = x * available
    stack.append(area)

print(max(stack))
