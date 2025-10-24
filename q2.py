def convert_temperature(temp,unit):
    if unit == "C":
        temp = round((9 * temp) / 5 + 32 , 2)
        return(f"the temperature Fahrenheit is: {temp} F")
    elif unit == "F":
        temp = round ((temp - 32) * 5 / 9, 2)
        return(f"the temperature Celsius is: {temp} C")
    else:
        return("f {unit} is an invalid unit of measurement")