import sys

input=sys.stdin.readline


people = int(input().strip())
size = list(map(int,input().split()))
bundle= list(map(int,input().split()))
shirts=0
pencil_bundle=0
pencil_single=0

for i in size:
    if int(i)%int(bundle[0])==0:
        shirts+=int(i)//int(bundle[0])

    elif int(i)%int(bundle[0])!=0:
        shirts += int(i)//int(bundle[0])+1

pencil_bundle=people//int(bundle[1])
pencil_single=people%int(bundle[1])

print("{}\n{} {}".format(shirts,pencil_bundle,pencil_single))


    

    


            

