n = str(input())
nlist = list(n)
yearno = 0
weekno = 0
if int(nlist[3]) <= 2:
    yearno = int(nlist[3]) * 10 + int(nlist[4])
    weekno = int(nlist[5]) * 10 + int(nlist[6])
else:
    yearno = int(nlist[3])
    weekno = int(nlist[4]) * 10 + int(nlist[5])
print(str(2000 + yearno) + "," +  str(weekno)) 
