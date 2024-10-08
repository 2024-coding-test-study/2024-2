from collections import deque

repeat_num = int(input())  # 반복 횟수 입력

for _ in range(repeat_num):
    commend = input()  # RRD, RDR 등의 명령어 입력
    list_total_index = int(input())  # 배열 크기
    element = input()  # 배열 요소 입력
    
    if element == "[]":
        list_element = deque()
    else :
        list_element = deque(int(x) for x in element.strip("[]").split(",") if x.strip().isdigit())
    
    reverse = False
    check = True

    for j in commend:  # 명령어 직접 순회
        if j == 'R':
            reverse = not reverse
        elif j == 'D':
            if not list_element:  # 리스트가 비어 있으면 error 출력
                check = False
                break
            else:
                if reverse:
                    list_element.pop()  # 뒤에서 제거
                else:
                    list_element.popleft()  # 앞에서 제거

    if check:
        if reverse:
            list_element.reverse()  # 역순 출력
        print(f"[{','.join(map(str, list_element))}]")
    else:
        print("error")
