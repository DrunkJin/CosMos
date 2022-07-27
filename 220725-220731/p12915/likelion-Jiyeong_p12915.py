# 1차 시도 성공했으나 다른 사람들에 비해서 코드가 김
# def solution(strings, n):
#     answer = []
#     dict = {}
#     strings.sort()
#     temp= [x[n] for x in strings]
#     for idx,val in enumerate(temp):
#         dict[idx] = val
    
#     dict_sort = sorted(dict.items(), key=lambda x: x[1])
#     answer = sorted([strings[x[0]] for x in dict_sort], key=lambda x:x[n])
    
#     return answer

# 2줄만에 짤 수 있는 문제였음. 
def solution(strings, n):
    strings.sort()
    answer = sorted(strings, key=lambda x:x[n])
    print(f"answer >> {answer}")
solution(["abce", "abcd", "cdx"],2)

