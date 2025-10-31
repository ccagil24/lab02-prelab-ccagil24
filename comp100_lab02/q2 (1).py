def draw(i):
    """
    Returns a string of the number i with spaces before it.
    """
    assert i > 0
    spaces = ""
    k = 1
    while k < i:
        spaces = spaces + "  "
        k = k + 1
    return spaces + str(i)


def make_wave(n, h):
    """
    Generates a number wave pattern for given n and h without using flags or direction indicators.
    """
    res = ""
    cycle = n * 2 - 2        # bir tam dalganın uzunluğu
    line = 0

    while line < h:
        # Dalganın içindeki konum
        pos = line % cycle

        # Yukarı çıkış ve inişin doğal akışı
        if pos < n:
            level = pos + 1
        else:
            level = cycle - pos + 1

        # Satırı ekle
        if res != "":
            res = res + "\n"
        res = res + draw(level)

        line = line + 1

    return res