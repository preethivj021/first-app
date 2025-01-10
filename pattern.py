'''for i in range(5):
    for j in range(4-i):
        print('',end=" ")

    for k in range(i+1):
       print('*',end="")

    print()
    
for a in range(5):
    for b in range(a):
        print(' ',end="")
    for c in range(5-a) :
        print('*',end="")
    print()
    '''
'''i=0
a=[10,20,30,40,50]
while i<=len(a)-1:
    print(a[i])
    i+=1'''
i=0
s=0
a=[10,20,30,40,50]
g=len(a)
for i in a:
    s=s+i
  
    print('total bill ',s)
    print('avg bill ',s/g)
