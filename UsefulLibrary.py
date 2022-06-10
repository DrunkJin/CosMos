"""
1. 기본 내장 함수 : print(), input(), sorted()와 같은 기본 문법처럼 쓰이는 함수들
2. itertools : 반복되는 형태의 데이터 처리 기능 제공 라이브러리. 수녕ㄹ과 조합 라이브러리 제공
3. heapq : 힙(Heap) 기능 제공 라이브러리. 우선순위 큐 기능을 구현하기 위해서 사용함.
4. bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리
5. collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리
"""

# 내장함수 : sum(), min(), max(), eval(), sorted()

# 나머진 익숙하니까.. eval()은 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환함
eval_result = eval("(3 + 5) * 7")
print(f"eval() 함수 실행 결과 : {eval_result}\n")


"""
itertools : 반복되는 데이터를 처리하는 기능을 포함하는 라이브러리

코테에서 가장 유용한 클래스 : permutations, combinations

permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산해줌.

combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산해줌
"""

# permutations
from itertools import permutations

data = ['A','B','C'] # 데이터 준비
result = list(permutations(data, 3)) # 3개를 뽑아 나열하는 모든 경우 구하기

print(f"permutations 걸과 : {result}\n")


# combinations
from itertools import combinations

data = ['A','B','C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(f"combinations 결과 : {result}\n")

"""
heapq : 다익스트라 최단 경로 알고리즘 및 우선순위 큐 기능 구현할 때 사용
힙에 원소를 삽입할 때는 heapq.heappop() 메서드 사용
최소힙으로 구성되어 있어서 단순히 원소들을 힙에 넣었다가 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료됨
"""
import heapq
# 최소 힙
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 왜 h인지는 나도 아직 잘 모르겠음
    return result
# 힙에 넣었다가 빼는 것만으로도 오름차순 정렬이 되는 듯함.
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(f"heapq 걸과 : {result}\n")

# 최대 힙을 제공하지 않아서 부호를 임시로 변경하고 넣고 다시 빼는 방법을 사용함
# 내림차순 정렬 구현 예시
def heapsort_reverse(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort_reverse([1,3,5,7,9,2,4,6,8,0])
print(f"heapq_reverse 걸과 : {result}\n")

"""
bisect : 이진 탐색을 쉽게 구현! 정렬된 배열에서 특정한 원소를 찾아야 할때 매우 효과적으로 사용됨
bisect_left(), bisect_right() 2개가 가장 중요하게 사용됨. 시간복잡도 O(logN)에 동작함
 * bisect_left(a, x) : 정렬된 순서를 유지하면서 list a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
 * bisect_right(a, x) : 정렬된 순서를 유지하면서 list a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

[1,2,4,4,8]에 새로운 데이터 4를 삽입하려 한다고 했을때,
bisect_left(a, 4) => 2
bisect_right(a, 4) => 4
1 2 (left) 4 4 (right) 8
"""
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(f"bisect_left(a, x) : {bisect_left(a, x)}")
print(f"bisect_right(a, x) : {bisect_right(a, x)}\n")

# '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용됨
# 아래는 그 예제
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(f"값이 4인 데이터 개수 출력 : {count_by_range(a, 4, 4)}")
print(f"값이 [-1, 3] 범위에 있는 데이터 개수 출력 : {count_by_range(a, -1, 3)}\n")


"""
collections : 유용한 자료구조를 제공
코테에서 유용하게 사용되는 것은 deque, Counter

deque를 사용해서 큐를 구현한다.
append(), pop()를 사용하는 것은 데이터 개수에 따라서 많은 시간이 소요될 수 있다. 

deque는 첫번째 원소를 제거할때 popleft()를 사용하고 마지막 원소를 제거할때 pop()
x를 삽입시에 첫번째에 넣을 때는 appendleft(x), 마지막에 넣을때는 append(x)

따라서 deque를 큐 자료구조로 이용할 때, 원소를 삽입할 때는 append(), 원소를 삭제할 때는 popleft()를 사용하면 된다.
이렇게 사용하면 먼저 들어온 원소가 항상 먼저 나가게 된다.


Counter는 등장 횟수를 세는 기능을 제공함. 리스트와 같은 iterable 객체에서 내부 원소가 몇번씩 등장했는지 알려준다.
원소별 등장 횟수를 세는 기능이 필요할 때 짧은 코드로 구현할 수 있다.
"""
# 리스트 [2,3,4]를 이용하는 방법
from collections import deque

# 데이터 추가할 때
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(f"데이터를 앞,뒤로 넣은 deque : {data}")
print(f"deque를 리스트형으로 변환한 것 : {list(data)}\n")

# 데이터 삭제할 때
data.popleft() # 왼쪽 끝에 있던 1 삭제
data.pop() # 오른쪽 끝에 있던 5 삭제

print(f"데이터를 앞,뒤로 삭제한 deque : {data}")
print(f"deque를 리스트형으로 변환한 것 : {list(data)}\n")

# Counter 사용
from collections import Counter

counter  = Counter(['red','blue','red','green','blue','blue'])

print(f"red가 등장한 횟수 : {counter['red']}")
print(f"blue가 등장한 횟수 : {counter['blue']}")
print(f"green이 등장한 횟수 : {counter['green']}")
print(f"Counter를 사전 자료형으로 변환 : {dict(counter)}\n")


"""
math : 팩토리얼, 제곱근, 최대공약수 등을 계산해주는 기능. 수학 계산 문제시 활용
"""
import math

print(f"5팩토리얼 : {math.factorial(5)}")
print(f"7의제곱근 반환 : {math.sqrt(7)}")

# 최대 공약수는 gcd(a,b) 이용
print(f"21과 14의 최대공약수 : {math.gcd(21,14)}")

# 수학 상수도 제공
print(f"파이(pi) : {math.pi}")
print(f"자연상수 e : {math.e}")
