h1,m1,s1 = int(input()), int(input()), int(input())
h2,m2,s2 = int(input()), int(input()), int(input())
t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2
difference = t2 - t1
print(difference)
