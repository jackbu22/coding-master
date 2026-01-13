import sys

input = sys.stdin.readline

words_count= int(input())
words=[]
for i in range(words_count):
    
    words+=list(input().split())


words.sort()
# print(words)

only = []
qwer = ''
for i in words:
    if i != qwer:
        only.append(i)
        qwer = i
words = only

# print(words)

words_lens=[]

for i in words:
    words_lens.append(len(i))
# print(words_lens)

length=0
for i in words_lens:
    if length<i:
        length=i


words_plus=[]

for i in range(len(words)):
    plus=str(words_lens[i]).zfill(length) + words[i] ##zfill 이란 함수를 쓰면 2이 02 가 되고  10 이랑그러면 sort 할때 비교가 가능해져버림
    words_plus.append(plus)

# print(words_plus)
words_plus.sort()
# print(words_plus)

answer=[]
for i in words_plus:
    answer.append(i[length:])

# print(answer)

for i in answer:
    print(i)
