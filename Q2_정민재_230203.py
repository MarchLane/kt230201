# Q1 Answer template

def solution(lottos, win_nums):
    win = 0
    for lo in lottos :
        if lo in win_nums :
            win += 1
        
    if win == 6 :
        rank = 1
    elif win == 5 :
        rank = 2
    elif win == 4 :
        rank = 3
    elif win == 3 :
        rank = 4
    elif win == 2 :
        rank = 5
    elif win == 1 :
        rank = 6
    elif win == 0 :
        rank = 7
    
    for lo in lottos :
        if lo == 0 :
            win += 1
    
    if win == 6 :
        rank_ = 1
    elif win == 5 :
        rank_ = 2
    elif win == 4 :
        rank_ = 3
    elif win == 3 :
        rank_ = 4
    elif win == 2 :
        rank_ = 5
    elif win == 1 :
        rank_ = 6
    elif win == 0 :
        rank_ = 7

    if rank == 7 :
        rank = 6
    answer = [rank_, rank]
    return answer

lottos = [0,0,0,0,0,0]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)