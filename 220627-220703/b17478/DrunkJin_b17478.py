
times = int(input())

# 언더바 때문에 문장마다 변수를 지정해주었음
text1 = '''"재귀함수가 뭔가요?"'''
text2 = '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'''
text3 = '''마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'''
text4 = '''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''

text5 = '''"재귀함수가 뭔가요?"'''
text6 = '''"재귀함수는 자기 자신을 호출하는 함수라네"'''

text7 = '''라고 답변하였지.'''

# 언더바의 갯수를 상정할 변수, 다시 언더바를 삭제시킬 변수, text6은 단 한번 출력되기 때문에 그걸 처리해줄 cnt변수
underbar = 0
threshold = times
cnt = 1

def rewind_text(times, underbar, cnt):
    if times == 0:                                                           
        if cnt == 1:    # text6번을 출력하기 위한 구문
            print("____"*(underbar) + text1)
            print("____"*(underbar) + text6)
            return rewind_text(times, underbar, cnt-1)
        else:
            if underbar != 0:
                print("____"*(underbar) + text7)    # underbar+text7을 출력한다음 언더바를 그다음부터 줄여나감.
                return rewind_text(times, underbar-1, cnt)
            elif underbar == 0:         # 언더바가 모두 제거되면 text7을 출력하고 재귀함수 종료
                return print(text7)
        
    elif times != 0:
        print("____"*underbar + text1)
        print("____"*underbar + text2)
        print("____"*underbar + text3)
        print("____"*underbar + text4)
        return rewind_text(times-1, underbar+1, cnt) # 반복횟수를 하나씩 줄이고 underbar를 늘려가며 자기함수 호출
    else:
        print(f"times:{times}\nunderbar={underbar}\ncnt:{cnt}")

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
rewind_text(times, underbar, cnt)




# 아래는 백준 다른사람답안
# return으로 처리하지말고 그냥 함수호출하면 나중에 바깥 함수들까지 순차적으로 출력되는 구조였다.....맙소사

# def f(n, s):
#     print(s+'"재귀함수가 뭔가요?"')

#     if n == 0:
#         print(s+'"재귀함수는 자기 자신을 호출하는 함수라네"')
#     else:
#         print(s+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'
#         +s+'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'
#         +s+'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         f(n-1, s+"____")
#     print(s+'라고 답변하였지.')

# n = int(input())
# print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
# f(times, "")