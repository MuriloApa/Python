def n_primos(x):
    cont=0
    for i in range(1, x+1):
        div=0
        for j in range(1, i+1):
            if i%j==0:
                div=div+1
        if div==2:
            cont=cont+1
    return cont
