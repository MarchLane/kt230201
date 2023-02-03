# Q2 Answer template

def solution(numbers):
    a = 0
    answer = 0
    for a in range(0, 10) :
        answer += a
    for num in numbers :
        answer -= num
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)