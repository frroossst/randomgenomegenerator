import random
bpe=['A','C','T','G']
bpv=['A','C','U','G']
def genegene(x):
    i=0
    while i<a:
        print(random.choice(x),end=' ')
        i+=1
    print()
print("1. ",bpe)
print("2. ",bpv)
ch=int(input("select : "))
a=int(input("enter basepairs : "))
if ch==1:
    genegene(bpe)
elif ch==2:
    genegene(bpv)
else:
    print("invalid choice")
  

