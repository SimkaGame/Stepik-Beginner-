num = int(input())
kol = 0
maxx = -99999
new_kol = 0
while num > 0:
    last_digital = num % 10
    num = num // 10
    kol += 1
    if last_digital > maxx:
        maxx = last_digital
        new_kol +=1
if kol == new_kol:
    print("YES")
else:
    print("NO")