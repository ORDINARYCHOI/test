def s():
    sq = [int(x) for x in input().strip().split()]
    l = [input() for j in range(sq[0])]
    r = -1
    k = -1
    z = True
    now = 0
    while (r == -1):
        k += 1
        if k == sq[0]:
            return 0
        for i in range(sq[1]):
            if l[k][i] == 'J':
                r = sq[0] - k - 1
                break
    li = [[-1, -1], [-1, -1]]
    for i in range(sq[1]):
        if l[sq[0] - 1][i] == 'J':
            if li[0][0] == -1:
                li[0][0] = i
            li[0][1] = i
    for i in reversed(range(k, sq[0] - 1)):
        for j in range(sq[1]):
            if l[i][j] == 'J':
                if li[1][0] == -1:
                    li[1][0] = j
                li[1][1] = j
        if z:
            if li[0][1] < li[1][1] and now < li[1][1]:
                if now < li[1][1]:
                    r += li[1][1] - now
                    now = li[1][1]
            elif li[0][1] >= li[1][1] and li[0][1] != -1:
                if now < li[0][1]:
                    r += li[0][1] - now
                    now = li[0][1]
            z = False
        else:
            if li[0][0] < li[1][0] and li[0][0] != -1 or li[1][0] == -1 and li[0][0] != -1:
                if now > li[0][0]:
                    r += now - li[0][0]
                    now = li[0][0]
            elif li[0][0] >= li[1][0] != -1 or li[0][0] == -1 and li[1][0] != -1:
                if now > li[1][0]:
                    r += now - li[1][0]
                    now = li[1][0]
            z = True
        li[0][0] = li[1][0]
        li[0][1] = li[1][1]
        li[1][0] = -1
        li[1][1] = -1
    if z:
        r += li[0][1] - now
    else:
        r += now - li[0][0]

    return r


print(s())
