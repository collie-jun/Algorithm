# 백준 8958
# 사용자로부터 정수 N을 입력
N = int(input())

# N개의 테스트 케이스를 처리하기 위해 반복문을 실행
for i in range(N):
    # 각 테스트 케이스의 OX 퀴즈 결과 문자열을 입력받음
    a = input()
    
    # score는 연속된 'O'의 점수를 계산하는 변수
    score = 0
    # sumScore는 해당 테스트 케이스의 총 점수를 저장하는 변수
    sumScore = 0
    
    # 입력받은 문자열의 각 문자에 대해 반복
    for j in a:
        # 현재 문자가 'O'라면
        if j == 'O':
            # 연속된 'O'의 수를 증가시켜 점수를 증가
            score += 1
        else:
            # 문자가 'X'라면 연속이 끊기므로 score를 0으로 초기화
            score = 0
        # sumScore에 현재 score를 더함
        sumScore += score
    
    # 최종적으로 계산된 해당 테스트 케이스의 총 점수를 출력
    print(sumScore)
