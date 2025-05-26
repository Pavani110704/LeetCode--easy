x = 121

lis = list(str(x)[::-1])

result = int("".join(map(str, lis)))
if result == x:
    print("T")
