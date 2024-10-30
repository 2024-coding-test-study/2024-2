import sys
import heapq

repaet_num = int(sys.stdin.readline())
max_haep = []
output = []


for i in range(repaet_num) :
    num = int(sys.stdin.readline())
    
    if num == 0:
        if not max_haep:
            output.append('0')
        else :
            output.append(str(-heapq.heappop(max_haep)))
    else :
        heapq.heappush(max_haep, -num)
        
print('\n'.join(output))