def int_to_roman(num):
    s = ''
    a=num//1000
    b=num-(a*1000)
    c = b // 500
    d = b - (c * 500)
    e = d // 100
    f=d-(e*100)
    g=f//50
    h=f-(g*50)
    i=h//10
    j=h-(i*10)
    k=j//5
    l=j-(k*5)
    m=l//1
    while a>=1:
        s=s+'M'
        a=a-1
    while c>=1:
        s=s+'D'
        c=c-1
    while e>=1:
        s=s+'C'
        e=e-1
    while g>=1:
        s=s+'L'
        g=g-1
    while i>=1:
        s=s+'X'
        i=i-1
    while k>=1:
        s=s+'V'
        k=k-1
    while m>=1:
        s=s+'I'
        m=m-1

    return s
