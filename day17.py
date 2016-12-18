import hashlib

#input="hijkl"
input="edjrjqaa"
dstring = "UDLR"

dirs=[(0,-1),(0,1),(-1,0),(1,0)]
opens="bcdef"

loc=(0,0)
visited={}


def make_cells(tuple,sofar,input):
    (x,y)=tuple
    s = input+sofar
    s=s.encode('utf-8')
    h = hashlib.md5(s).hexdigest()[0:4]
    newcells = [ ((x+dirs[i][0],y+dirs[i][1]),sofar+dstring[i])
                 for i in range(4) if h[i] in opens
                 and x+dirs[i][0]>=0 and y+dirs[i][1]>=0
                 and (x+dirs[i][0],y+dirs[i][1],sofar+dstring[i] not in visited)]
    return newcells

dones=[]

def search(loc,dest,input):
    q=[]
    # current, sofar
    q.append((loc,""))
    while q:
        #print(q)
        (current,sofar) = q[0]
        visited[(current,sofar)]=sofar
        q=q[1:]

        if (current==dest):
            dones.append(len(sofar))
            print(len(sofar))
            continue
        
        nexts = make_cells(current,sofar,input)
        q=q+nexts
        

    
search((0,0),(3,3),input)
print(max(dones))
