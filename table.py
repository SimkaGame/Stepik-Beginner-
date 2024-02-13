number = int(input())
count_cycle = 0
count = 0
while count != number:
    if count_cycle != 9:
        count +=1
        for j in range(9):
            print(count,"+",count_cycle + 1,"=", count + count_cycle +1)
            count_cycle +=1
    else:
        count_cycle = 0
        print()
        