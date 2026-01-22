n = int(input())

members = []
for i in range(n):
    age,name = map(str, input().split())
    age = int(age)

    dict = {"age" : age,
             "name" : name}
    members.append(dict)

members = sorted(members, key=lambda x: x["age"])


for i in members:
    print(i['age'], i['name'])