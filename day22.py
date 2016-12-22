import re

expr = r".*x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T.*"



l="/dev/grid/node-x0-y0     85T   64T    21T   75%"
drives=[]
for l in open("day22.dat").readlines():
    m = re.match(expr,l)
    t = [x for x in m.groups()]
    
    drives.append({'x': t[0],'y':t[1],'size':t[2],'u':t[3],'a':t[4]})

print( drives[0:10])
