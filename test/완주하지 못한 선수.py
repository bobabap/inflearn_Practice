# 1차

def solution(participant, completion):
    for p in participant:
        if participant.count(p) > completion.count(p):
            return p

a = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(a)

# 2차
def solution(participant, completion):
    player = list(set(participant)-set(completion))
    if player:
        return player[0]

a = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(a)

#3차
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop() # participant.sort() => ["eden", "kiki", "leo"]
                             # completion.sort()  => ["eden", "kiki"]
a = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(a)

