import sys

n = int(sys.stdin.readline())
result = 0

while n > 0:
    if n % 5 == 0:
        result += n // 5
        n = 0
        break
    else:
        n -= 3
        result += 1

if n:
    print(-1)
else:
    print(result)