def int_to_roman(num):
    s = ''
    a = num // 1000
    b = (num % 1000) // 100
    c = (num % 100) // 10
    d = num % 10
    while a >= 1:
        s += 'M'
        a -= 1
    while b >= 1:
        if b == 9:
            s += 'CM'
            b -= 9
        if b >= 5:
            s += 'D'
            b -= 5
        if b == 4:
            s += 'CD'
            b -= 4
        if b >= 1:
            s += 'C'
            b -= 1
    while c >= 1:
        if c == 9:
            s += 'XC'
            c -= 9
        if c >= 5:
            s += 'L'
            c -= 5
        if c == 4:
            s += 'XL'
            c -= 4
        if c >= 1:
            s += 'X'
            c -= 1
    while d >= 1:
        if d == 9:
            s += 'IX'
            d -= 9
        if d >= 5:
            s += 'V'
            d -= 5
        if d == 4:
            s += 'IV'
            d-=4
        if d >= 1:
            s += 'I'
            d -= 1
    return s
