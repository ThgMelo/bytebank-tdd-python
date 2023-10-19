# ByteBank TDD - Python
Reposiório do curso da plataforma alura.    
**Python e TDD: Explorando testes unitários**

## Executando o projeto em ambiente de desenvolvimento

1. Criar: `python -m venv venv`
O primeiro **venv** refere-se a *virtual environment*, o ambiente de desenvolvimento que estamos criando. O segundo é o nome do ambiente.
 
2. Ativar: `python source venv/bin/activate`

## Pytest
1. Instalação: `pip install pytest`
2. Na pasta **tests** ficarão os arquivos de testes
3. O arquivo **__init__.py** é o *dunder init*.

### Rodando o teste
Basta digitar no terminal: `pytest`     
     
Para um relatório mais detalhado, basta digitar no terminal: `pytest -v`    
      
Podemos executar um específico informando apenas uma palavra do método: `pyteste -v -k idade` porém esse método de filtrar pelo nome pode executar testes que não queríamos.     
Para solucionar isso podemos import o mark de pytest e incluir decorators nos métodos. Para cada decorator iremos informar o nome.     
Para rodar `pytest -v -m calcular_bonus`     
O arquivo **pytest.ini** contém as configurações do pytest e podemos configurarnovos markers.    
Ao rodar `pytest -v -m calcular_bonus`  não veremos mais warnings porque criamos o arquivo de configuração