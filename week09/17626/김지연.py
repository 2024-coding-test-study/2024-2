n = int(input())

lst = [5] * (n+1)
lst[0] = 0
lst[1], lst[2] = 1, 2
for target in range(3, n+1):
    for i in range(1, target//2+1):
        #targetd을 만들 수 있는 두 자연수
        if target / i == float(i):
            lst[target] = 1
            break
        lst[target] = min(lst[target], lst[target-i] + lst[i])
    # print(lst)
print(lst[n])