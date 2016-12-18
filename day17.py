import hashlib

#input="hijkl"
input="edjrjqaa"
dstring = "UDLR"

dirs=[(0,-1),(0,1),(-1,0),(1,0)]
opens=set("bcdef")

loc=(0,0)
visited={}


def make_cells(tuple,sofar,input):
    (x,y)=tuple
    s = input+sofar
    s=s.encode('utf-8')
    h = hashlib.md5(s).hexdigest()[0:4]
    newcells = [ ((x+dirs[i][0],y+dirs[i][1]),sofar+dstring[i])
                 for i in range(4) if
                 x+dirs[i][0]>=0 and y+dirs[i][1]>=0
                 and
                 h[i] in opens
                 
                 
                 
                 and (x+dirs[i][0],y+dirs[i][1],sofar+dstring[i] not in visited)]
    return newcells

def make_cells_fast(tuple,sofar,input):
    (x,y)=tuple
    s = input+sofar
    s=s.encode('utf-8')
    h = hashlib.md5(s).hexdigest()
    q=[]
    if x+1<4 and h[3] in opens:
        q.append( ((x+1,y),sofar+dstring[3]))
    if x-1>=0  and h[2] in opens:
        q.append( ((x-1,y),sofar+dstring[2]))
    if y+1<4 and h[1] in opens:
        q.append( ((x,y+1),sofar+dstring[1]))
    if y-1>=0 and h[0] in opens:
        q.append( ((x,y-1),sofar+dstring[0]))
    return q


                                    

dones=[]

def search(loc,dest,input):
    q=[]
    max=0
    sol=""
    # current, sofar
    q.append((loc,""))
    while q:
        (current,sofar) = q.pop(0)
        visited[(current,sofar)]=sofar

        if (current==dest):
            sol=sofar
            #print(len(sofar))
            #print(sofar)
            #return
        else:
            nexts = make_cells_fast(current,sofar,input)
            q=q+nexts
            
                                                                                                                                                                                                            
    return len(sol)
print(search((0,0),(3,3),input))
#print(max(dones))
