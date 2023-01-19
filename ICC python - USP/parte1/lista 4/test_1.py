def maximo (x, y):
    if x>y:
        return x
    else:
        return y
def teste_max():
    assert maximo(45,2)==45
def teste_max2():
    assert maximo(5,2)==5
def teste_max3():
    assert maximo(-12,0)==0
