# ler-xml-nfe-python
Script em python para ler um repositório com xml de nota fiscais eletronica.

Testado no python 3.7

1) Baixe o projeto em sua máquina local (git clone https://github.com/3bears-data/ler-xml-nfe-python.git)
2) Instale o virtualenv caso seu python não tenha (python -m pip install --user virtualenv)
3) Acesse a pasta do projeto e crie o ambiente (python -m venv venv)
4) Instale o requirements (.\venv\Scripts\pip.exe install -r requirements.txt)
5) Crie duas pastas, nfe e convert
6) Cole suas nfe dentro da pasta nfe.
7) Execute o script (.\venv\Scripts\python.exe main.py)

O script irá percorrer pela pasta local nfe, capturando os arquivos xml, fará a conversão do xml para dataframe e por fim converterá cada arquivo xml em csv, a ser salvo na pasta convert.
