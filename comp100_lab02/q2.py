def draw(i):
    s = ""
    k = 1
    while k < i:
        s += " "
        k += 1
    return s + str(i)


def make_Wave(n, h):
    result = ""   
    if n == 1:
        line = 0
        while line < h:
            if result != "":
                result += "\n"
            result += draw(1)
            line += 1
        return result

    cycle = n * 2 - 2
    line = 0

    while line < h:
        pos = line % cycle
        if pos < n:
            lvl = pos + 1
        else:
            lvl = cycle - pos + 1

        if result != "":
            result += "\n"

        result += draw(lvl)
        line += 1

    return result
    
      
