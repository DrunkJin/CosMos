
s = int(input()) 

calculation = 0 # 1���� ��� ���� ���� ��
number = 0 # 1���� �����ϴ� ��

while True:
    if calculation > s: # calculation�� s���� ũ�ٸ� �� ���̸�ŭ�� ���ڸ� �����ؾ��ϹǷ� number-1
        print(number-1)
        break
    elif calculation == s: # calculation�� s�� �����ϴٸ� number������ ���̹Ƿ� number ���
        print(number)
        break
    else: # calculation�� s���� �۴ٸ� ����ؼ� number ���� ������Ű�鼭 ����
        number += 1
        calculation += number
