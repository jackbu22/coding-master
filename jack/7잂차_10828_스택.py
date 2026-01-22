# #getattr 함수 getattr(리스트나 문자열이나 뭐 이런거,함수 이름)(input)
# n=['pop']
# m=['1']
# q=['1','1','1','1','1','1','1']
# q.n[0](int(m[0]))
# print(getattr(q,n[0])(int(m[0])))

import sys

input= sys.stdin.readline

numbers=int(input())
methods=[]
class qwer:
    def push(self,x=int):
        self.append(x)
    def pop(self,x=int):
        if len(self)==0:
            print('-1')
        elif len(self)!=0:
            print(self[-1])
            self.pop() #remove는 필요할때만 쓰자!
    def size(self,x=int):
        print(len(self))
    def empty(self,x=int):
        if len(self)==0:
            print('1')
        elif len(self)!=0:
            print('0')
    def top(self,x=int):
        if len(self)==0:
            print('-1')
        else:
            print(self[-1])
# push(methods,1)
# push(methods,2)
# print(methods)

# pop(methods,1)
# size(methods,0)
# empty(methods,0)
# top(methods,0)


for i in range(numbers):
    
    x=input()
    methods.append(x)


# print(methods)
methods_1=[]
for i in methods:
    i=i[0:-1]
    if i[-1].isdigit()==False:
        i=i+' 0'
    methods_1.append(i)
# print(methods_1)
real_method=[]
number=[]
for i in methods_1:
    a,b=i.split()
    real_method.append(a)
    number.append(b)
# print(real_method)
# print(number)
answer=[]
for i in range(len(number)):
    getattr(qwer,real_method[i])(answer,int(number[i]))
# print(answer)
