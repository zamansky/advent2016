dirs=[(0,1),(0,-1),(1,0),(-1,0)]

steps={}
walls={}
def set_wall(x,y):
    walls[(x,y)]=True
    
def is_wall(x,y):
    v=x*x+3*x+2*x*y+y+y*y+code
    s="{0:b}".format(v)
    return  s.count("1") % 2 != 0
        

def next_positions(x,y):
    p = [ (x+a,y+b) for (a,b) in dirs if x+a>=0 and y+b>=0
          and (x+a,y+b) not in steps and (x+a,y+b) not in walls]
          

    #print(walls)
    [ set_wall(x,y)  for (x,y) in p if is_wall(x,y)  ]
    p=[(x,y) for (x,y) in p if (x,y) not in walls]
    return p

def clear():
    print("[2J")
    
def draw():
    print("[0;0H")
    for (x,y) in steps:
        print("[{};{}H.".format(x,y))
    for (x,y) in walls:
        print("[{};{}H#".format(x,y))

def search(start,dest):
    (x,y)=start
    q=[(x,y)]
    steps[(x,y)]=1
    while len(q)>0:
        (x,y) = q[0]
        if (x,y)==dest:
            break
        q = q[1:]
        nexts = next_positions(x,y)
        for (a,b) in nexts:
            steps[(a,b)] = steps[(x,y)] +1
        q = q + nexts
        #step = step + 1
        #print(walls)
        #print(steps)
        #print(q)
        #print()
        #draw()
        #input()
        draw()
    
    #print()
    
    print("[52;0H")
    print(steps[dest]-1)
        

def p2(start,dest):
    (x,y)=start
    q=[(x,y)]
    steps[(x,y)]=1
    while len(q)>0:
        (x,y) = q[0]
        q = q[1:]
        nexts = next_positions(x,y)
        for (a,b) in nexts:
            steps[(a,b)] = steps[(x,y)] +1
        q = q + nexts
        draw()
    
    #print()
    
    print("[52;0H")
    #print(steps[dest])
    sanswer = [(x,y) for (x,y) in steps if steps[(x,y)]<=50]
    print("Part 2:",len(sanswer)+1)

clear()

code=1350
dest=(31,39)
#code=10
#dest=(7,4)
#search((1,1),dest)
p2((1,1),dest)

