def draw(i):
    spaces = ""
    k = 1
    while k < i:
        spaces = spaces + "  "
        k = k + 1
    return spaces + str(i)
def make_wave(n, h):
    res = ""
    if n == 1:
        line = 0
        while line < h:
            if res != "":
                res = res + "\n"
            res = res + draw(1)
            line = line + 1
        return res
    cycle = n * 2 - 2
    line = 0
    while line < h:
        pos = line % cycle
        if pos < n:
            level = pos + 1
        else:
            level = cycle - pos + 1
        if res != "":
            res = res + "\n"
        res = res + draw(level)
        line = line + 1
    return res