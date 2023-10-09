numbersi = set()
numbers = input().split()
for num in numbers:
    if num in numbersi:
        print('YES')
    else:
        numbersi.add(num)
        print("NO")