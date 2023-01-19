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
def test_primo():
    assert maior_primo(100)==97

def test_primo2():
    assert maior_primo(101)==101

def test_primo3():
    assert maior_primo(102)==101

def test_primo4():
    assert maior_primo(35)==31

def test_primo5():
    assert maior_primo(961)==953