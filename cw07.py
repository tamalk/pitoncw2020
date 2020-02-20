ant = 0
n = 1
m = int(input())
for i in range(m):
  while (i <= len(m) - 1):
    print(n, end='-')
    if (i == len(m)):
      print(n)
  ant, n = n, ant+n
