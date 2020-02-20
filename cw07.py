ant = 0
n = 1
m = int(input())
for i in range(m):
    if (i <= (m-2)):
        print(str(n), end='-')
    else:
        print(n)
    ant, n = n, ant+n
