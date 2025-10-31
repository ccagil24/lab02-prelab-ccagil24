def format_factor(factor, power):
    if power > 1:
       text = str(factor) + "^" + str(power)
    else:
       text = str(factor)
    return text
    