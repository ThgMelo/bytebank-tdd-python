from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' #Given-contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado # Then-desfecho

    def test_quando_nome_recebe_Thiago_Melo_deve_retornar_Melo(self):
        entrada = ' Thiago Melo'
        esperado = 'Melo'

        thiago = Funcionario(entrada, '08/07/1999', 10000)
        resultado = thiago.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    def test_retorno_str_(self):
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000
        esperado = 'Funcionário(Teste, 12/03/2000, 1000)'
        
        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado