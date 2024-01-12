[![Standard](https://github.com/ZyamHunter/pypy-rpaframework-tables/actions/workflows/standard.yaml/badge.svg)](https://github.com/ZyamHunter/pypy-rpaframework-tables/actions/workflows/standard.yaml)

# pypy-rpaframework-tables
Repositório de testes dedicados ao uso da biblioteca rpaframework com tables utilizando o compilador pypy ao invés do cpython

# robot
> Repositório de testes dedicados ao uso da bibliotecas rpaframework com json 

# Configuração do Ambiente

## 1. Instalar PyPy 3.10
- https://www.pypy.org/download.html

## 2. Se estiver usando Windows, download do Microsoft Visual C++
- https://www.microsoft.com/en-us/download/details.aspx?id=52685
> Adicione o diretório do PyPy ao PATH das variáveis de ambiente
- ex: C:\Program Files\pypy3.10-v7.3.14-win64

## 3. Criar um ambiente virtual:
- pypy3 -m venv venv

## 4. Se você estiver usando o PowerShell e encontrar problemas para executar scripts, talvez precise alterar a política de execução temporariamente para permitir a execução de scripts:
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

## 5. Ativar o ambiente virtual:
- venv\Scripts\activate

## 6. Remover cache do pip
- pip cache remove *

## 7. Rodar os testes
- pypy3 run_tests.py

## 8. Desativar ambiente virtual
- deactivate

## 9. Instalar dependências do Projeto
> Primeiro ative o ambiente virtual para evitar erros de versão com outras bibliotecas instaladas
- pypy3 -m pip install -r requirements.txt

<br/>

### ---- Diferenciais no projeto ----
<br/>

- Page Object
- RPA Framework
- PyPy3
- Massa de Dados

<br/>
