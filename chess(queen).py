a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c == a + 1 and d == b + 1 or c == a + 2 and d == b + 2 or c == a + 3 and d == b + 3 or c == a + 4 and d == b + 4 or c == a + 5 and d == b + 5 or c == a + 6 and d == b + 6 or c == a + 7 and d == b + 7 or c == a - 1 and d == b - 1 or c == a - 2 and d == b - 2 or c == a - 3 and d == b - 3 or c == a - 4 and d == b - 4 or c == a - 5 and d == b - 5 or c == a - 6 and d == b - 6 or c == a - 7 and d == b - 7 or c == a - 1 and d == b + 1 or c == a - 2 and d == b + 2 or c == a - 3 and d == b + 3 or c == a - 4 and d == b + 4 or c == a - 5 and d == b + 5 or c == a - 6 and d == b + 6 or c == a - 7 and d == b + 7 or c == a + 1 and d == b - 1 or c == a + 2 and d == b - 2 or c == a + 3 and d == b - 3 or c == a + 4 and d == b - 4 or c == a + 5 and d == b - 5 or c == a + 6 and d == b - 6 or c == a + 7 and d == b - 7:
    print("YES")
elif a == c:
    print("YES")
elif b == d:
    print("YES")
else:
    print("NO")