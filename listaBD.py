import json

rutaRegistro1 = "/home/paxauz/projects/python/agencia_de_buses/usuarios.json"



with open(rutaRegistro1, 'r') as u:
    usuarios = json.load(u)
    for usuario in usuarios:
        if usuario["admin"]:
            print(usuario)