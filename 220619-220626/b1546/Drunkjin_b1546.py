# N개의 과목수
# 최고점 M. 다른 과목을 (x / M) * 100으로 바꿈. 
# 새로운 평균점수는?

n = int(input())    #  과목 수 입력
scores = list(map(int, input().split()))    # 과목 성적 입력해서 리스트로 바꿔줌

m = max(scores) # 최고 점수 저장

new = list(map(lambda x: (x/m)*100, scores))    # 성적들을 문제에서 제공한 식으로 모두 계산

new_average = sum(new)/n    # 변경한 점수들의 평균 계산

print(new_average)