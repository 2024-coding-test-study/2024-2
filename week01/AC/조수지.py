# 32분 소요

from collections import deque

t = int(input())

for _ in range(t) :
    func = list(input())  # 함수 입력받기
    n = int(input())
    input_list = input()

    if n == 0 :
        nums = deque()  # 빈 리스트 생성
    else :
        nums = deque(map(int, input_list.strip('[]').split(',')))  # 대괄호 제거 후 ,를 기준으로 리스트화 시킴

    # R 여부를 판단하지 않고 무작정 reverse()를 실행하면 시간 초과
    if_reverse = False  # R 실행 여부 판단

    for f in func :
        if f == 'R' :  # R 실행
            if_reverse = not if_reverse  # R 여부만 바꿔줌. 실제 적용은 마지막에.
        
        else :  # D 실행
            if not nums :  # nums가 비어있을 때
                print("error")
                break
            
            elif if_reverse :  # R이 홀수번 입력 되었을 때
                nums.pop()  # 아직 실제로 reverse하지 않았기에 오른쪽 끝에서 pop
            
            else :  # R이 입력되지 않았거나 짝수번 입력 되었을 때
                nums.popleft()  # 왼쪽 끝에서 POP

    else :  # 에러가 없을 때만 출력
        if if_reverse :
            nums.reverse()

        print("[" + ",".join(map(str, nums)) + "]")
