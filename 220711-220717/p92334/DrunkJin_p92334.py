def solution(id_list, report, k):
    #0. �ߺ��� �Ű�� ������
    report = list(set(report))
    report_dic = {}
    answer_dic = {}
    #1. ����Ʈ Ƚ���� �����ϴ� ��ųʸ� ����
    for i in report:
        violator = i.split()[1]
        if violator in report_dic:
            report_dic[violator] += 1
        else:
            report_dic[violator] = 1
    #2. ���� ���� Ƚ���� �˱� ���� ��ųʸ� ����
    for member in id_list:
        answer_dic[member] = 0
    
    #3. ����Ʈ�� ���� violator���� report_dic���� k�̻��� ���̸� reporter�� 1�� ������
    for i in report:
        reporter = i.split()[0]
        violator = i.split()[1]
        if report_dic[violator] >= k:
            answer_dic[reporter] += 1

    return list(answer_dic.values())

    """
�׽�Ʈ 1 ��	��� (0.02ms, 10.3MB)
�׽�Ʈ 2 ��	��� (0.03ms, 10.3MB)
�׽�Ʈ 3 ��	��� (211.24ms, 39.3MB)
�׽�Ʈ 4 ��	��� (0.04ms, 10.2MB)
�׽�Ʈ 5 ��	��� (0.04ms, 10.2MB)
�׽�Ʈ 6 ��	��� (1.27ms, 10.3MB)
�׽�Ʈ 7 ��	��� (1.80ms, 10.7MB)
�׽�Ʈ 8 ��	��� (2.32ms, 10.9MB)
�׽�Ʈ 9 ��	��� (98.43ms, 23.9MB)
�׽�Ʈ 10 ��	��� (79.50ms, 23.8MB)
�׽�Ʈ 11 ��	��� (197.73ms, 39.4MB)
�׽�Ʈ 12 ��	��� (0.24ms, 10.2MB)
�׽�Ʈ 13 ��	��� (0.33ms, 10.4MB)
�׽�Ʈ 14 ��	��� (66.73ms, 20MB)
�׽�Ʈ 15 ��	��� (150.11ms, 31.3MB)
�׽�Ʈ 16 ��	��� (0.28ms, 10.4MB)
�׽�Ʈ 17 ��	��� (0.22ms, 10.4MB)
�׽�Ʈ 18 ��	��� (0.48ms, 10.3MB)
�׽�Ʈ 19 ��	��� (0.74ms, 10.3MB)
�׽�Ʈ 20 ��	��� (63.30ms, 20MB)
�׽�Ʈ 21 ��	��� (101.23ms, 31.4MB)
�׽�Ʈ 22 ��	��� (0.01ms, 10.1MB)
�׽�Ʈ 23 ��	��� (0.01ms, 10.1MB)
�׽�Ʈ 24 ��	��� (0.01ms, 10.3MB)
    """