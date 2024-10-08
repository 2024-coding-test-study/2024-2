# 1h 12m

k = int(input()) # 참외 개수

all_ = [] # 밭의 모든 변을 저장할 배열
width = [] # 가로변 저장할 배열
length = [] # 세로변 저장할 배열

for _ in range(6) :
  dir, len = map(int, input().split())
  
  if dir == 1 or dir == 2 : # 동, 서 방향일 때 가로변 저장
    all_.append(len)
    width.append(len)
     
  else : # 남, 북 방향일 때 세로변 저장
    all_.append(len)
    length.append(len)
    
# 가장 긴 가로, 세로변의 index 구하기
long_width_index = all_.index(max(width))
long_length_index = all_.index(max(length))

# 작은 직사각형의 가로세로 구하기
small_width = all_[(long_length_index + 3) % 6]
small_length = all_[(long_width_index + 3) % 6]

big = max(width) * max(length)
small = small_length * small_width

square = big - small

print(square * k)