
num = int(input())
total = 0
for i in range(num) :
    list = []
    string = input()
    spaced_string = ' '.join(string)
    
    for j in spaced_string.split():
        
        if len(list) != 0:
            list.append(j)
            if list[-1] == list[-2] :
                list.pop()
                list.pop()
        else :
            list.append(j)
    if len(list) == 0 :
        total+=1  
print(total)        