def main():
    testa_mais_curto()


def mais_curto(names_list):
    menor = 0
    for i in range(1,len(names_list)):
        if len(names_list[i].strip()) < len(names_list[menor].strip()):
            menor = i
    return names_list[menor].strip().capitalize()
    
def testa_mais_curto():
    assert "Menor" == mais_curto(["menor                                                                                             ", "paralelepipedo", "pneumoutramicroscopicossilicovulcanoconiotico"])


main()
