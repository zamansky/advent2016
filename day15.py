
#disks=[(5,4),(2,1)]

disks=[(17,15),(3,2),(19,4),(13,2),(7,2),(5,0)]
#part 2
disks.append((11,0))

x = [x for x in enumerate(disks,1)]

time = 0
while True:
    totals = [ (time+pos+e)%max for e,(max,pos) in x]
    if sum(totals)==0:
        break
    time = time + 1
print(time)
