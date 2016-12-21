
def swap_pos_xy(s,x,y):
    
    s = list(s)
    tmp = s[x]
    s[x]=s[y]
    s[y]=tmp
    return("".join(s))

def swap_letter_xy(s,a,b):
    x=s.find(b)
    y=s.find(a)
        
    return swap_pos_xy(s,x,y)

def rotate_right(s,n):
    splitpoint = len(s)-n
    a=s[:splitpoint]
    b=s[splitpoint:]
    return b+a 

def rotate_left(s,n):
    splitpoint = n
    a=s[:splitpoint]
    b=s[splitpoint:]
    return b+a

def rotate_pos(s,letter):
    pos = s.find(letter)
    s = rotate_right(s,1)
    if pos>=4:
        pos = pos + 1
    pos = (pos )%8
    s = rotate_right(s,pos)
    return s

def unrotate_pos(s,letter):
    import itertools
    for p in itertools.permutations(s):
        ps = "".join(p)
        if s==rotate_pos(ps,letter):
            print(ps)
            return ps
    return s 
def rev(s,a,b):
    
    if a>b:
        tmp=b
        b=a
        a=tmp
    b=b+1
    r = s[a:b]
    s=s[0:a]+r[::-1] + s[b:]
    return s

def move(s,a,b):
    c = s[a]
    s = s[:a]+s[a+1:]
    s=s[:b]+c+s[b:]
    return s
def unmove(s,a,b):
    c = s[b]
    s = s[:b]+s[b+1:]
    s=s[:a]+c+s[a:]
    return s

def part1(line,s):
    line = line.split()
    if line[0]=='rotate':
        if line[1]=="right":
            s = rotate_right(s,int(line[2]))
        elif line[1]=="left":
            s = rotate_left(s,int(line[2]))
        else:
            s = rotate_pos(s,line[6])
    elif line[0]=="reverse":
        s = rev(s,int(line[2]),int(line[4]))
    elif line[0]=="move":
        s = move(s,int(line[2]),int(line[5]))
    elif line[0]=="swap":
        if line[1]=="position":
            
            s = swap_pos_xy(s,int(line[2]),int(line[5]))
        else:
            s = swap_letter_xy(s,line[2],line[5])
    else:
        print("UNKNOWN:",line)

    return s



def part2(line,s):
    line = line.split()
    if line[0]=='rotate':
        if line[1]=="right":
            s = rotate_left(s,int(line[2]))
        elif line[1]=="left":
            s = rotate_right(s,int(line[2]))
        else:
            s = unrotate_pos(s,line[6])
    elif line[0]=="reverse":
        s = rev(s,int(line[2]),int(line[4]))
    elif line[0]=="move":
        s = unmove(s,int(line[2]),int(line[5]))
    elif line[0]=="swap":
        if line[1]=="position":
            
            s = swap_pos_xy(s,int(line[2]),int(line[5]))
        else:
            s = swap_letter_xy(s,line[2],line[5])
    else:
        print("UNKNOWN:",line)

    return s



if __name__=="__main__":
    input = open("day21.dat").readlines()
    s = "abcdefgh"
    for l in input:
        s = part1(l,s)
    print(s)

    s="fbgdceah"
    input = open("day21.dat").readlines()
    for l in reversed(input):
         s = part2(l,s)
    print(s)

    
