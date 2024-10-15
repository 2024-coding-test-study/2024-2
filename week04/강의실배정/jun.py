import sys
input = sys.stdin.read
data = input().splitlines()

repeat_num = int(data[0])
start_time = []
end_time = []

for i in range(1, repeat_num + 1):
    start, end = map(int, data[i].split())
    start_time.append(start)
    end_time.append(end)

cnt = repeat_num

for i in range(repeat_num):
    cmp_end = end_time[i]

    for j in range(repeat_num):
        cpm_start = start_time[j]

        if cpm_start >= cmp_end:
            cnt -= 1
        break

print(1 if cnt == 0 else cnt)
