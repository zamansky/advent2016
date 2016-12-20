

input = open("day20.dat").readlines()

 
lines = [
    [int(x),int(y)] for (x,y) in [x.strip().split("-") for x in input]

]


    
lines = sorted(lines,key=lambda x: x[0])

i=1
while i<len(lines):
    if lines[i][0] > lines[i-1][1]:
        i=i+1
        continue
    if lines[i][1]>lines[i-1][1]:
        lines[i-1][1]=lines[i][1]
    del(lines[i])

part1Done=False
totalIps=0
for i in range(1,len(lines)):
    if lines[i][0]-lines[i-1][1]!=1:
        if not part1Done:
            print(lines[i-1][1]+1)
            part1Done=True
        diff = lines[i][0]-lines[i-1][1]-1
        totalIps = totalIps + diff

print(totalIps)

        



