import sys

input= sys.stdin.readline

count= int(input().strip())

people=[]
age1=[]
name1=[]
for i in range(count):
    age,name= input().split()
    age1.append(age)
    name1.append(name)
# print(age1,name1)  

length=0

for i in age1:
    if length < len(i):
        length= len(i)

age2=[]

for i in age1:
    age2.append(i.zfill(length))

plus_age_name=[]

for i in range(len(age2)):
    order=str(i).zfill(len(str(len(age2))))
    plus=age2[i]+order+name1[i]
    plus_age_name.append(plus)
    
    
plus_age_name.sort()
# print(plus_age_name)
answer_list=[]
for i in plus_age_name:
    answer= str(int(i[:length]))+' '+i[length+len(str(len(age2))):]
    answer_list.append(answer)


# print(answer_list)
# print(people)
for i in answer_list:
    print(i)

# 메모리 부족 
