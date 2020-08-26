# PyNFSe
[![Code Climate](https://codeclimate.com/github/marcelobelli/PyNFSe/badges/gpa.svg)](https://codeclimate.com/github/marcelobelli/PyNFSe)
[![Build Status](https://travis-ci.org/marcelobelli/PyNFSe.svg?branch=master)](https://travis-ci.org/marcelobelli/PyNFSe)
[![Coverage Status](https://coveralls.io/repos/github/marcelobelli/PyNFSe/badge.svg?branch=master)](https://coveralls.io/github/marcelobelli/PyNFSe?branch=master)

A biblioteca PyNFSe funciona como um facilitador para os desenvolvedores que precisam gerir a emissão de Nota Fiscal de Serviços por meio eletrônico. As funcionalidades desta biblioteca são:

* Criação dos XMLs de RPS (Recibo Provisório de Serviço)
* Criação dos XML dos Lotes RPS.
* Envio dos lotes de RPSs, realizando a comunicação com o webservice da respectiva prefeitura
* Consulta e Cancelamento de NFS-es emitidas

Além disso a PyNFSe possui uma CLI para operação via linha de comando.

## Cidades Atendidas

* Curitiba

## Instalação

Via PyPI
```console
pip install PyNFSe
```

ou
```console
git clone https://github.com/marcelobelli/PyNFSe.git
cd PyNFSe
pip install -r requirements.txt
```

## Problemas

* Descobrir o problema de conexão quando atualiza o requests
para versões superiores a 2.11.1 e o cryptography está instalado

## Roadmap

* Tornar disponível no PyPI
* Adicionar novas cidades
* Documentação

## REST Server
REST Server.
To Start:
```
gunicorn -b 0.0.0.0:8000 "rest:create_app()" &
```

To Call: 
```
time curl -X POST  localhost:8000/api -H 'Content-Type: application/json' -d '{"tomador": {"razao_social": "Nome Cliente","tipo_documento": "CNPJ","numero_documento": "12345678000123","endereco": "Rua Cliente","endereco_numero": "1234","bairro": "Bairro Cliente","codigo_municipio": "4106902","uf": "PR","cep": "80000000","telefone": "4132221122","email": "financeiro@cliente.com.br"},"servico": {"valor_servico": 1000.00,"iss_retido": 2,"item_lista": "1401","discriminacao": "Descrição do Serviço Prestado","codigo_municipio": "4106902","codigo_cnae": 9511800,"codigo_tributacao_municipio": "1401","aliquota": "0.02"},"rps": {"identificador": "N1","year": 2016,"month": 12,"day": 12,"hour": 17,"minutes": 22,"seconds": 39,"miliseconds": 960610,"simples": 1,"incentivo": 2,"numero": 1,"serie": "A1","tipo": "1","natureza_operacao": 1}}' -i
```

To validate if service is alive:
```
curl localhost:8000/health
```
