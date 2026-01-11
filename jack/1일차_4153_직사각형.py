import sys
input=sys.stdin.readline

while True:
    Q = list(map(int,input().split()))
    Q.sort()
    a= Q[0]
    b= Q[1]
    c= Q[2]
    if a==0 or b==0 or c==0:
        break


    if c*c==a*a + b*b:
        print("right")
    elif c**2 != a**2 +b **2:
        print("wrong")

