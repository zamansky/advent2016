import re

expr = r".*x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T.*"



l="/dev/grid/node-x0-y0     85T   64T    21T   75%"
drives=[]
for l in open("day22.dat").readlines():
    m = re.match(expr,l)
    t = [x for x in m.groups()]
    
    drives.append({'x': int(t[0]),'y':int(t[1]),'size':int(t[2]),'u':int(t[3]),'a':int(t[4])})


byuse = sorted(drives,key=lambda x: x['u'],reverse=True)
byavail = sorted(drives,key=lambda x: x['a'],reverse=True)
print( byuse[0:10])
print( byavail[0:10])

for item in byuse:
    fits = [x for x in byavail if x['a'] >= item['u']]
    print(fits)
    print(len(fits))
