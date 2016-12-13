regnames="abcd"
# regvals=[0,0,0,0] # for part 1
regvals=[0,0,1,0] # for part 2


def cpy(x,y):
    if x in regnames:
        xval = regvals[ord(x)-97]
    else:
        xval = int(x)
    regvals[ord(y)-97]=xval

def inc(x):
    ri=ord(x)-97
    regvals[ri] = regvals[ri]+1

def dec(x):
    ri=ord(x)-97
    regvals[ri] = regvals[ri]-1

def jnz(x,y):
    if x in regnames:
        ri = ord(x)-97
    else:
        ri = int(x)
        
    if regvals[ri]!=0:
        ipo=int(y)
    else:
        ipo=0
    return ipo


def run(commands):
    ip=0;
    while ip < len(commands):
        #print("ip=",ip)
        c = commands[ip]
        #print("command:",c)
        if c.startswith("cpy"):
            (cmd,x,y) = c.split()
            cpy(x,y)
        elif c.startswith("inc"):
            (cmd,x) = c.split()
            inc(x)
        elif c.startswith("dec"):
            (cmd,x) = c.split()
            dec(x)
        elif c.startswith("jnz"):
            (cmd,x,y) = c.split()
            ipo = jnz(x,y)
            if ipo != 0:
                ip = ip + ipo -1
                
        ip = ip + 1
 
input = open("day12.dat").readlines()
commands = [l.strip() for l in input]
run(commands)
print(regvals)
