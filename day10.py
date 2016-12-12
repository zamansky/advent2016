import re

input=open("day10.dat").readlines()
instructions=[]
outputs={}
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
                    

while True:
    
    for inst in instructions:
        if inst[0] in robots and len(robots[inst[0]]["chips"])  <2:
            pass
        else:
            # do the move
            # we're done when we find out compares 61 and 17
            try:
                chips = robots[inst[0]]['chips']
            except:
                continue
            small = min(chips)
            big = max(chips)
            robots[inst[0]]["chips"].remove(small)
            robots[inst[0]]["chips"].remove(big)
            print(small,big)
            if small==17 and big==61:
                print("DONE:", inst[0])
                sys.exit(0)
            if inst[1]=="bot":
                robots.setdefault(inst[2],{})
                robots[inst[2]].setdefault('chips',[])
                robots[inst[2]]['chips'].append(small)
            else:
                outputs[inst[2]]=small
            if inst[3]=="bot":
                robots.setdefault(inst[4],{})
                robots[inst[4]].setdefault('chips',[])
                robots[inst[4]]['chips'].append(big)
            else:
                outputs[inst[4]]=small
    print(outputs)
