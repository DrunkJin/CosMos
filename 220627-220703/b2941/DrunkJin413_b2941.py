
target = input()


croatia = ['c=','c-','dz=','d-','lj','nj','s=','z='] # 바꿔야하는 크로아티아문자

for word in croatia:
    target = target.replace(word,'o') # 1개의 알파벳으로 변환
    

print(len(target)) # 변환된 단어의 길이 출력