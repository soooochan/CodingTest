time = list(map(int, input().split()))


if time[1] < 45:
    time[1] = time[1] + 60 - 45
    if time[0] == 0:
        time[0] = 24
    time[0] = time[0] - 1
else:
    time[1] = time[1] - 45

print(time[0], time[1])
