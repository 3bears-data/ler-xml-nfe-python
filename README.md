# ler-xml-nfe-python
Script em python para ler um repositório com xml de nota fiscais eletronica.

Testado no python 3.7

1) Baixe o projeto em sua máquina local (git clone https://github.com/3bears-data/ler-xml-nfe-python.git)

2) Instale as libs do requirements.txt (pip install -r requirements.txt)

3) Crie uma pasta dentro do projeto por nome de nfe e outra por nome de convert.

4) Coloque as suas notas dentro da pasta nfe e em seguida, execute o script main.py.

O script irá percorrer pela pasta local nfe, capturando os arquivos xml, fará a conversão do xml para dataframe e por fim ele converterá cada arquivo xml em csv, a ser salvo na pasta convert.
