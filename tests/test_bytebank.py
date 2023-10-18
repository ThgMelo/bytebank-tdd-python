from codigo.bytebank import Funcionario

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