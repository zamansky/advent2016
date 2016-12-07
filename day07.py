import re
input = open("/home/zamansky/gh/advent2016/day07.dat").readlines()


print(input[0])


expr = r"([a-z])((?!\1)[a-z])\2\1"
hexpr = r"[a-z]*(\[[a-z]+\])[a-z]*"
hremexpr = r"\[[a-z]+\]"
     
def part1(input):
    count=0
    for item in input:
        hexprs = " ".join(re.findall(hexpr,item))
        rexprs = re.sub(hremexpr," ",item)
        if re.search(expr,rexprs) and not re.search(expr,hexprs):
            count = count + 1
    return count

def part2(input):
    count=0
    for item in input:
        hexprs = " ".join(re.findall(hexpr,item))
        rexprs = re.sub(hremexpr," ",item)

        for i in range(len(rexprs)-2):
            aba=rexprs[i:i+3]
            if aba[0]!=aba[2] or aba[0]==aba[1]:
                continue
            rev = aba[1]+aba[0]+aba[1]
            if rev in hexprs:
                count = count + 1
                break;
    return count                
                 
