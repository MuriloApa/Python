def fatorial (x):
	if x<0:
		return 0
	pot=1
	for i in range(1, x+1):
		pot=pot*i
	return pot

def test_fat1():
    assert fatorial(5)==120
def test_fat2():
    assert fatorial(0)==1
def test_fat3():
    assert fatorial(-6)==0