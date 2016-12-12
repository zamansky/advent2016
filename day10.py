import re

input=open("day10.dat").readlines()
instructions=[]
robots={}
for line in input:
    line = line.rstrip("\n")
    if "value"==line[0:5]:
        matcho = r"[a-z ]+([0-9]+)[a-z ]+([0-9]+).*"
        m=re.match(matcho,line)
        val = m.group(1)
        robot=m.group(2)
        robots.setdefault(robot,{})
        robots[robot].setdefault("chips",[])
        robots[robot]["chips"].append(val)
    else:
        matcho=r"bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)"
        m=re.match(matcho,line)
        instructions.append((m.group(1),m.group(2),m.group(3),m.group(4),m.group(5)))
                    
            
for inst in instructions:
    robots.setdefault(robot,{})
    robots[robot].setdefault("chips",[])

    if inst[0] in robots and len(robots[inst[0]]["chips"]) < 2:
        continue
    else:
        # do the move
        # we're done when we find out compares 61 and 17
        pass

        
