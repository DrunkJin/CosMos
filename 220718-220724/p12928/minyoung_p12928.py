def solution(number):
    index = 1

    result = 0

    while index <= number:
        if number % index == 0:
            result  += index

        index +=1
        
    return result