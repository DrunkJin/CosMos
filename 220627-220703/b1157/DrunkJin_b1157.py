
word = input()

word = word.upper() # ��� �빮�ڷ� ��ȯ

if len(set(word)) == 1: # �Ѱ��� ���ڷ� �̷���� ��� �ϳ� ���
    print(word[0])
    
else:
    count_dict = {} # ���ĺ� ���� �� ��ųʸ� ����
    for alpha in word: # �ܾ�� ���ĺ��� �ϳ��� �־
        if alpha in count_dict: # ��ųʸ��� ���ĺ��� �ִٸ� +1
            count_dict[alpha] += 1
            
        else: #��ųʸ��� ���ĺ��� ���ٸ� 1 ����
            count_dict[alpha] = 1 

    sort_count_dict = sorted(count_dict, key = lambda x : count_dict[x], reverse=True) # ������ ��ųʸ��� �������� ���� => Ű���� �����������ķ� ����Ʈ���·� �����

    if count_dict[sort_count_dict[0]] == count_dict[sort_count_dict[1]]: # ��ųʸ����� �����ص� ����Ʈ���� ù��°�� �ι�°�� value���� ���ٸ� ����ǥ ���
        print("?")

    else:
        print(sort_count_dict[0]) # �� �̿ܿ��� ����Ʈ ù��°�� ���