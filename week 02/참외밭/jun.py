count_melon = int(input())

max_height = 0
max_weight = 0
max_height_idx = 0
max_weight_idx = 0

location = [0 for _ in range(6)]
data = [0 for _ in range(6)]

for i in range(6) :
    line = input()
    values = list(map(int, line.split()))
    location[i] = values[0]
    data[i] = values[1]
    
for i in range(6) :
    if location[i] == 1 or location[i] == 2: #가로 
        if(data[i] > max_weight) :
            max_weight = data[i]
            max_weight_idx = i
    else :                                    # 세로
        if(data[i] > max_height) :
            max_height = data[i]
            max_height_idx = i
        
min_height = data[(max_height_idx+3)%6]
min_weight = data[(max_weight_idx+3)%6]

total = (max_height*max_weight) - (min_height*min_weight)

print(total*count_melon)