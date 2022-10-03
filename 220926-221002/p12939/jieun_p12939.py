def solution(s):
    integer = list(map(int,s.split()))
    return str(min(integer))+' '+str(max(integer))