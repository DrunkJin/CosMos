def solution(phone_number):
    answer = ''
    for _ in phone_number[:-4]: # ���� 4�ڸ� ���� ������ �ڸ��� �����ϴ� ��ŭ �ݺ��ϸ� * �ֱ�
        answer += "*"
    answer += phone_number[-4:] # �� 4�ڸ� ���̱�
    return answer