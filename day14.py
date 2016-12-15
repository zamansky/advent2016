import hashlib, re
import sys
#salt="abc"
salt = "qzyelonm"
PART=2

pad_keys=[]
keys=0
current=0
s = salt+str(current)
s = s.encode('utf-8')
h = hashlib.md5(s).hexdigest()
hashes={}

rethree=r"([0-9a-z])\1\1"

def hasfive(digit,current):
    scan=current+1
    refive = digit*5
    while scan < current+1000:
        if scan in hashes:
            h = hashes[scan]
        else:
            s = salt+str(scan)
            s = s.encode('utf-8')
            h = myhash(s,PART)
            hashes[scan]=h
                        
        
        if re.search(refive,h):
            return True
        scan = scan + 1
    return False

        


def myhash(s,part=1):
    i = 1;
    h = hashlib.md5(s).hexdigest()
    if part==2:
        for i in range(2016):
            h=hashlib.md5(h).hexdigest()
    return h

while keys <= 63:
    if current in hashes:
        h = hashes[current]
    else:
        s = salt+str(current)
        s = s.encode('utf-8')
        #h = hashlib.md5(s).hexdigest()
        h = myhash(s,PART)
        hashes[current]=h

    f = re.findall(rethree,h)
    if len(f)>0:
        print(current)
        if hasfive(f[0],current):
            
            keys=keys+1
            pad_keys.append(current)
            
            
    current=current+1

print(current-1)
    
