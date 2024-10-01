k = int(input())

#4->1, 2->1 1->3은 공통으로 작은 사각형
#서, 남쪽에서 시작할때: 3->2 도 작은 사각형
data = []
for i in range(6):
    direction, length = map(int, input().split())
    data.append((direction, length))
i = 0
small_area = 0
big_area = 0
while i <= 6: # data리스트에 대해서 한번 다 돌았다면 멈추기
    direction1, length1 = data[i%len(data)][0], data[i%6][1]
    direction2, length2 = data[(i+1)%len(data)][0], data[(i+1)%len(data)][1]
    if direction1 == 4 and direction2 == 1 or direction1 == 2 and direction2 == 1 or direction1 == 1 and direction2 == 3:
        small_area = length1 * length2
        #참외밭에서 작은 영역을 구했다면 작은 영역의 길이 전 후의 길이를 각각 더하면 전체 밭의 넓이를 알 수 있음.
        big_area = (data[(i-1)%len(data)][1] + length2) * (data[(i+1+1)%len(data)][1] + length1)
        break
    if data[0][0] == 2 or data[0][0] == 3: #서, 남에서 시작할 때의 예외 추가
        if direction1 == 3 and direction2 == 2:
            small_area = length1 * length2
            big_area = (data[(i-1)%len(data)][1] + length2) * (data[(i+1+1)%len(data)][1] + length1)
            break
    i += 1

result_area = big_area - small_area
print(result_area * k)