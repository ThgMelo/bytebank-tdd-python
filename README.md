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


### Cobertura de testes
Ao comparar lado a lado os arquivos **bytebank.py** e **test_bytebank.py**, podemos concluir que não há garantia de que todas as linhas de código estão cobertas por algum teste. Quando trabalhamos com testes, a intenção é ter 100% de cobertura por testes.     
Para ter a garantia que todo o código será testado podemos usar a extensão **pytest-cov**. *Cov - coverage = cobertura*

#### pytest-cov
1. Instalação: `pip install pytest-cov`
2. Executar: `pytest --cov=codigo tests/` Com isso descobrimos quantos porcentagem está coberto
3. Relatório dos termos faltantes: `pytest --cov=codigo tests/ --cov-report term-missing`
4. Relatório HTML: `pytest --cov=codigo tests/ --cov-report html`

### Ignorando linhas
O pytest-covnos informar quanto de nossa classe está sendo testado, porém, podemos ignorar alguns desses testes.    
Para isso criamos o arquivo **.coveragerc** e dentro informaremos os nomes dos métodos que queremos que ignore se foi testado ou não

### Gerando relarórios
Incluindo a informação `source = ./codigo` no arquivo **.coveragerc** podemos reduzir a sintaxe para gerar relatório: `pytest --cov`

#### Alterando pasta que salva o relatório html
Incluir a informação abaixo no arquivo **.coveragerc** 
```
[html]
directory = coverage_relatorio_html
```

Rodar: `pytest --cov=codigo tests/ --cov-report html`

### pytest.ini
Podemos adotar no arquivo **pytest.ini** para que toda vez que executarmos o pytest ele execute gerando os relatório, para isso basta alterar o arquivo incluindo:
```
addopts = -v --cov=codigo tests/ --cov-report term-missing
```

Após isso, para gerar o relatório basta digitar no terminal: `pytest`

### Relatórios em xml
`pytest --junitxml report.xml`