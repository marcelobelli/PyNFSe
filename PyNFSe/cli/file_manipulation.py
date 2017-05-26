import json
import pickle

def file_create(filename):
    with open(filename, mode='w') as file:
        json.dump({}, file)

def append_json(filename, value):
    with open(filename, mode='r') as file:
        json_file = json.load(file)

    with open(filename, mode='w') as file:
        json_file.append(value)
        json.dump(json_file, file, ensure_ascii=False)

def add_client(clients_file, client_dict):
    with open(clients_file, mode='r') as file:
        json_file = json.load(file)

    index = client_dict['numero_documento']
    client_json = json.dumps(client_dict, ensure_ascii=False)

    with open(clients_file, mode='w') as file:
        json_file[index] = (client_json)
        json.dump(json_file, file, ensure_ascii=False)
