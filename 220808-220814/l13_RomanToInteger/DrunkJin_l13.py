class Solution:
    def romanToInt(self, s: str) -> int:
        # 로마자 사전 생성
        roman = {'I':1, 'V':5, 'X':10, 
                 'L':50, "C":100, "D":500, "M":1000}
        
        # 로마자를 정수형 리스트로 변환
        s_list = list(map(lambda x:roman[x], s))
        
        prev = 9999999
        answer = 0

        # 일단 모두 더한 다음에 만약 이전 숫자가 현재보다 크다면 이전 숫자를 2번 빼줌
        # ex. 1000 10 100 10 => 1000 + 10 + 100 - 20 + 10
        for i in s_list:
            answer += i
            if prev < i:
                answer -= 2*prev
            prev = i
        return answer

        """
        Runtime: 64 ms, faster than 72.16% of Python3 online submissions for Roman to Integer.
        Memory Usage: 13.9 MB, less than 31.19% of Python3 online submissions for Roman to Integer.
        """