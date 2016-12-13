import re
import sys
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
        robots[robot]["chips"].append(int(val))
    else:
        matcho=r"bot ([0-9]+) gives low to (bot|output) ([0-9]+) and high to (bot|output) ([0-9]+)"
        m=re.match(matcho,line)
        instructions.append((m.group(1),m.group(2),m.group(3),m.group(4),m.group(5)))
                    


while True:
    if "0" in outputs and "1" in outputs and "2" in outputs:
        print(outputs["0"]*outputs["1"]*outputs["2"])
        sys.exit(0);
    
    for inst in instructions:
        if inst[0] in robots and len(robots[inst[0]]["chips"])  <2:
            pass
        else:
            # do the move
            # we're done when we find out compares 61 and 17
            if inst[0] not in robots:
                continue
            chips = robots[inst[0]]['chips']
            small = min(chips)
            big = max(chips)
            robots[inst[0]]["chips"].remove(small)
            robots[inst[0]]["chips"].remove(big)
            print("ZZZ",small,big,inst[1],inst[2],inst[3],inst[4])
            #if small==17 and big==61:
            #    print("DONE:", inst[0])
            #    sys.exit(0)
            if inst[1]=="bot":
                robots.setdefault(inst[2],{})
                robots[inst[2]].setdefault('chips',[])
                robots[inst[2]]['chips'].append(small)
                print(robots[inst[2]])
            else:
                outputs[inst[2]]=small
            if inst[3]=="bot":
                robots.setdefault(inst[4],{})
                robots[inst[4]].setdefault('chips',[])
                robots[inst[4]]['chips'].append(big)
                print(robots[inst[4]])
            else:
                outputs[inst[4]]=big
        
