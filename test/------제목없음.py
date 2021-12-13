
def solution(n, lost, reserve):
    
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    print('set_reserve', set_reserve)
    print('set_lost',set_lost)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

a = solution(5, [2,4,5], [1,3,5])
print(a)