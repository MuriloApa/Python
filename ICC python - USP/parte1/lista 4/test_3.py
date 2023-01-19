def vogal(letra):
    if  (letra=='a' or letra=='A' or letra=='e' or letra=='E' or letra=='i' or letra=='I' or letra=='o' or letra=='O' or letra=='u' or letra=='U'):
        return True
    else:
        return False

def test_vogal1():
    assert vogal('a')==True

def test_vogal2():
    assert vogal('b')==False

def test_vogal3():
    assert vogal('U')==True