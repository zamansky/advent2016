import re
import sys


def decompress(input):
    output=""
    while len(input)>0:
        matcho=re.compile("\(([0-9]+)x([0-9]+)\)")
        s = re.search(matcho,input)
    
        if not s:
            output = output+input
            break
        #print(input[0:60])
        #print(s.group())
        si=s.start()
        ei=s.end()
        chars = int(s.group(1))
        times = int(s.group(2))
        #print(input[si:ei],si,ei,chars,times)
        #print("\n\n\n")
        output = output + input[0:si]
        block=input[ei:ei+chars]
        b=block*times
        output=output+b
        input = input[ei+chars:]

    return output

def de2(input):
    output=""
    o=0
    while len(input)>0:
        matcho=re.compile("\(([0-9]+)x([0-9]+)\)")
        s = re.search(matcho,input)
    
        if not s:
            o=len(input)
            
            return o
        si=s.start()
        ei=s.end()
        chars = int(s.group(1))
        times = int(s.group(2))
        #print(input[si:ei],si,ei,chars,times)
        #print("\n\n\n")
        
        output = output + input[0:si]
        to = len(output)
        
        block=input[ei:ei+chars]
        
        block = decompress(block)
        o=o+to+len(block)*times
        input = input[ei+chars:]

    return o

 
input = open("day09.dat").read()

# print(decompress("ADVENT"))
# print("\n===================================\n")
# print(decompress("A(1x5)BC"))
# print("\n===================================\n")
# print(decompress("(3x3)XYZ"))
# print("\n===================================\n")
# print(decompress("A(2x2)B(2x2)EFG"))pr
# print("\n===================================\n")
# print(decompress("(6x1)(1x3)A"))
# print("\n===================================\n")
# print(decompress("X(8x2)(3x3)ABCY"))
# print("\n===================================\n")
input.strip()
input=input.replace(" ","")
input=input.replace("\t","")
input=input.replace("\n","")

print(len(decompress(input)))
print(de2(input))
