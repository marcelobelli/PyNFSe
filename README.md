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
