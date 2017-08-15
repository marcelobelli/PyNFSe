import json
import os

from PyNFSe.nfse.pr.curitiba import NFSeCuritiba


def home_folder():
    return os.path.expanduser('~')


def criar_diretorio(directory):
    path = os.path.join(home_folder(), directory)

    try:
        os.mkdir(path)
        print('Diretório {} criado'.format(directory))
    except FileExistsError:
        print('O diretório {} já existe'.format(directory))


def criar_arquivo_json(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w') as file:
            json.dump({}, file)
        print('Arquivo {} criado'.format(filename))
        return True
    else:
        print('O arquivo {} já existe'.format(filename))
        return False


def salvar_arquivo_json(arquivo_json, obj):
    with open(arquivo_json, mode='w') as file:
        json.dump(obj.__dict__, file, ensure_ascii=False)


def enviar_lote(lote_rps, ambiente, producao):
    ambiente = ambiente
    cliente = NFSeCuritiba(ambiente.certificado, ambiente.senha, producao=producao)

    return cliente.recepcionar_lote_rps(lote_rps)
