def romantoint(numeral):
    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
    result = 0
    
    for i, j in zip(numeral, numeral[1:]):
        if roman[i] < roman[j]:
            result -= roman[i]
        else:
            result += roman[i]

    return result + roman[numeral[-1]]


print(romantoint("III"))
