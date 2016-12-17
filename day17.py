import hashlib
dstring = "UDLR"

dirs=[(0,-1),(0,1),(-1,0),(1,0)]


loc=(0,0)
visited={}


def make_cells(tuple,hash):
    s = hash
    s=s.encode('utf-8')
    h = hashlib.md5(s).hexdigest()[0:4]
    newcells = [ ((x+dirs[i][0],y+dirs[i][1]),hash+dstring[i],dstring[i])
                 for i in range(4) if h[i] in opens
                 and x+dirs[i][0]>=0 and y+dirs[i][1]>=0 ]
    return newcells


def search(loc,dest,h):
    q=[]
    # current, prev, hash, prevdir
    q.append((loc,dest,h,""))
    while q:
        pass
