a, b, c = int(input()), int(input()), int(input())
if b < a < c:
    print(a)
elif c < a < b:
    print(a)
if a < b < c:
    print(b)
elif c < b < a:
    print(b)
if a < c < b:
    print(c)
elif b < c < a:
    print(c)