n = int(input())
cnt = 0

while n > 0:
    while n >= 5:
        while n >= 10:
            while n >= 25:
                cnt += 1
                n -= 25
            cnt += 1
            n -= 10
        cnt += 1
        n -= 5
    cnt += 1
    n -= 1
print(cnt)