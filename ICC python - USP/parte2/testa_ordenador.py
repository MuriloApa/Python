import metodos_ordenacao
import pytest

class Testa_ordenador:

    @pytest.fixture
    def o(self):
        return metodos_ordenacao.Metodos_ordenacao()
    
    @pytest.fixture
    def l_quase(self):
        order = metodos_ordenacao.Metodos_ordenacao()
        return order.lista_quase_ordenada(10000)
    
    @pytest.fixture
    def l_aleatoria(self):
        order = metodos_ordenacao.Metodos_ordenacao()
        return order.lista_aleatoria(10000)
    
    def esta_ordenado(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                return False
        return True
    
    def test_bolha(self, o, l_aleatoria):
        o.bubblesort(l_aleatoria)
        assert self.esta_ordenado(l_aleatoria)

    def test_bolha_melhorado(self, o, l_aleatoria):
        o.bubblesort_melhorado(l_aleatoria)
        assert self.esta_ordenado(l_aleatoria)

    def test_insercao(self, o, l_aleatoria):
        o.insertionSort(l_aleatoria)
        assert self.esta_ordenado(l_aleatoria)

    def test_selection(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.esta_ordenado(l_aleatoria)
    

