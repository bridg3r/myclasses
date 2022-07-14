i = 1
j = 1
while i < 1000:
    if (-2 * i - 5 * j) % 3 == 0:
        print('i:', i, 'j:', j, 'k:', (-2 * i - 5 * j) / 3)
    i += 1
    j += 1


