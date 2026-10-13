
n, k = map(int, input().split())

scores = list(map(int, input().split()))

advancing = 0
threshold_score = scores[k - 1]

for score in scores:
    if score >= threshold_score and score > 0:
        advancing += 1

print(advancing)
