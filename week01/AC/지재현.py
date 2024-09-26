# import ast

# T = int(input())
# result = ""
# for _ in range(T):
#     command = input()
#     n = int(input())
#     arr = ast.literal_eval(input())
#     for c in command:
#         if c == 'R':
#             arr.reverse()
#         elif c == 'D':
#             if not arr:
#                 arr = "error"
#                 break
#             arr.pop(0)
    
#     if isinstance(arr, list):
#         result += str(arr).replace(" ", "")
#     else:
#         result += arr
#     if (_ != T-1):
#         result += "\n"
    
# print(result)

import ast

T = int(input())
result = []

for _ in range(T):
    command = input()  # 명령어 입력
    n = input()
    arr = ast.literal_eval(input())  # 배열 입력

    is_reversed = False  # 반전 상태를 추적
    error = False

    for c in command:
        if c == 'R':
            is_reversed = not is_reversed  # 반전 상태를 토글
        elif c == 'D':
            if not arr:
                result.append("error")
                error = True
                break
            if is_reversed:
                arr.pop()  # 반전 상태일 때 마지막 요소 제거
            else:
                arr.pop(0)  # 첫 번째 요소 제거

    if not error:  # error가 발생하지 않았을 경우
        if is_reversed:
            arr.reverse()  # 최종적으로 리스트를 반전
        result.append(str(arr).replace(" ", ""))  # 리스트를 문자열로 변환

print("\n".join(result))
