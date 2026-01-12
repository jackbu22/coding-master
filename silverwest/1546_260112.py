n = int(input())
scores = list(map(int, input().split()))
scores.sort()

max = scores[-1]

new_score = 0

for score in scores:
    new_score += score / max

print(new_score / n * 100)