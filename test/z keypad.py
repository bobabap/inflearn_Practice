def solution(numbers, hand):
    answer = ''

    # 키패드를 좌표로 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작 위치
    left_start = dic['*']
    right_start = dic['#']

    for i in numbers:
        now = dic[i]
        # 1, 4, 7을 누르는 경우 무조건 왼손으로
        if i in [1, 4, 7]:
            answer += "L"
            left_start = now
        
        # 3, 6, 9를 누르는 경우 무조건 오른손
        elif i in [3, 6, 9]:
            answer += "R"
            right_start = now
        
        # 2, 5, 8, 0을 누르는 경우
        else:
            left_distance = 0
            right_distance = 0

            # 좌표 거리 계산해주기
            for a, b, c in zip(left_start, right_start, now):
                left_distance += abs(a-c)
                right_distance += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if left_distance < right_distance:
                answer += "L"
                left_start = now
            
            # 오른손이 더 가까운 경우
            elif left_distance > right_distance:
                answer += "R"
                right_start = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이일 경우
                if hand == 'left':
                    answer += "L"
                    left_start = now
                
                #오른손잡이일 경우
                if hand == 'right':
                    answer += "R"
                    right_start = now
    return answer