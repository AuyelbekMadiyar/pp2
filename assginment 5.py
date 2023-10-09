n, m = map(int, input().split())
anya = set()
boris = set()
for i in range(n):
    color = int(input())
    anya.add(color)
for i in range(m):
    color = int(input())
    boris.add(color)

common_colors = anya.intersection(boris)

aniyas = anya - common_colors
borisk = boris - common_colors
print(len(common_colors))
print(*sorted(common_colors))
print(len(aniyas))
print(*sorted(aniyas))
print(len(borisk))
print(*sorted(borisk))

