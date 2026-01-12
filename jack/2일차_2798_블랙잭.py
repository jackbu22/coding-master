import sys

input=sys.stdin.readline

a,b = map(int,input().split())
card = list(map(int,input().split()))
answer = []
# print(a,b,card)
# print(card.index(5))
for i in card:
    for j in card[card.index(i)+1:]:
        for k in card[card.index(j)+1:]:
            plus=int(i)+int(j)+int(k)
            answer.append(plus)

answer.sort()
# print(answer)

while answer[-1] > b:
    answer.pop()

# print(answer)
print(answer[-1])

