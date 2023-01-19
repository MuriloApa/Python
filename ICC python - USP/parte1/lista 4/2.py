def maior_primo(x):
    i=x
    primo=2
    while i>=2 and primo==2:
        div=0
        for j in range(1, i+1):
            if i%j==0:
                div=div+1
        if div==2:
            primo=i
        i=i-1
    return primo