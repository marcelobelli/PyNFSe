import json
import os


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
    # path = os.path.join(home_folder(), directory)
    # file_path = os.path.join(path, filename)

    if not os.path.exists(filename):
        with open(filename, mode='w') as file:
            json.dump({}, file)
        print('Arquivo {} criado'.format(filename))
        return True
    else:
        print('O arquivo {} já existe'.format(filename))
        return False