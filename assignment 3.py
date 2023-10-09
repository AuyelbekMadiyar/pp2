set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
sovpodajut = sorted(set1 & set2)
for number in sovpodajut:
    print(number)