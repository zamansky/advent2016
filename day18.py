start=".^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^"
#rows=40

rows=400000

#start='.^^.^.^^^^'


safe = start.count(".")


def gennext(r):
    s=""
    r="."+r+"."
    for i in range(1,len(r)-1):
        triple = r[i-1:i+2]
        #print(triple)
        if triple=="^^." \
           or triple==".^^" \
           or triple=="^.." \
           or triple=="..^":
            s=s+"^"
        else:
            s=s+"."
    return s

nextrow=start
for i in range(rows-1):
    
    nextrow = gennext(nextrow)
    
    safe=safe+nextrow.count(".")

print(safe)
