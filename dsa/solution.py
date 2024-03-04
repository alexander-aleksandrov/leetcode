"""
ID: aleksan37
LANG: PYTHON3
TASK: ride
"""
d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
x = fin.readline().strip()
y = fin.readline().strip()
ans = ""
prod_1 = 1
prod_2 = 1
for i in x:
    prod_1 *= d[i]
for i in y:
    prod_2 *= d[i]
if prod_1 % 47 == prod_2 % 47:
    ans = "GO"
else:
    ans = "STAY" 
fout.write (ans + '\n')
fout.close()