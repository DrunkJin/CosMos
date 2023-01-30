"""
아직 해결 못함
"""
s= "{{2},{2,1},{2,1,3},{2,1,3,4}}"
answer = []
tmp = ''
for i in s:
    if i in ['{','}']:
        continue
    elif i == ',':
        answer.append(int(tmp))
        tmp = ''
        continue
    tmp += i
print(answer)