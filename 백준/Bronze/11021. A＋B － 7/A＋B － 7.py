num = int(input())

for i in range(1, num + 1):
    a, b = map(int, input().split())
    result = a + b
    print("Case #{}: {}".format(i, result))