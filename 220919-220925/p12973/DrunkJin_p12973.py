def solution(s):
    if len(s) % 2 == 1: return 0  # 홀수개라면 무조건 불가능
    if len(s) == 2:  # 문자가 2개이고, 같은 문자라면 무조건 가능
        return 1 if s[0] == s[1] else 0

    stack = [s[0]]  # 첫글자부터 넣어서 확인하고 넣고 뻄

    for i in s[1:]:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return 0 if len(stack) else 1