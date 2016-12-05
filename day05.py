import hashlib 
import sys

input="wtnhxymk"
index=0;
p=""
p2pw=[-1,-1,-1,-1,-1,-1,-1,-1]
pw2len=0
#while len(p)<8: # for part 1
while pw2len < 8:
    s = input+str(index)
    s=s.encode('utf-8')
    h = hashlib.md5(s).hexdigest()
    if h.startswith("00000"):
        print(s,h)
        p=p+h[5]
        try:
            pos=int(h[5])
            if p2pw[pos] == -1:
                p2pw[pos]=h[6]
                pw2len = pw2len + 1
        except:
            pass
    index=index+1
print("\n\n")
print(p)
print(p2pw)

    
    
