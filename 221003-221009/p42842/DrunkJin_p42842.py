def solution(brown, yellow):
    answer = []
    shape = brown + yellow
    plus_xy = -(brown+4)/2

    x1 = int(((-1*plus_xy)+(plus_xy**2 -4*shape)**(1/2))/2)
    x2 = int(((-1*plus_xy)-(plus_xy**2 -4*shape)**(1/2))/2)
    answer.append(x1)
    answer.append(x2)
    return answer


"""
정답을 x,y라고 하고 brown, yellow를 a,b라고 했을 때 다음 등식이 성립한다.

a+b = xy 
(x-2)(y-2) = b

아래 식을 풀어 쓰면, y = (xy + 4 - b) / (-2)
여기서 xy - b = a 이므로
y = ((a+4)/2) - x 가 성립한다.

xy = a+b 등식에 y=((a+4)/2)-2를 대입하면

x^2 + (-(a+4)/2)x - (a+b) = 0 이 나온다.

이 때 근의 공식을 통해 x를 구하면 된다.
"""