
target = input()


croatia = ['c=','c-','dz=','d-','lj','nj','s=','z='] # �ٲ���ϴ� ũ�ξ�Ƽ�ƹ���

for word in croatia:
    target = target.replace(word,'o') # 1���� ���ĺ����� ��ȯ
    

print(len(target)) # ��ȯ�� �ܾ��� ���� ���