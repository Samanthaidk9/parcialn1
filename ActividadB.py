import json


diccionario = {
    "Humancs": {
        "clases": ["guerrero", "jinete", "mago", "recolector", "observador"],
        "atributos": {
            "guerrero": {"vida": 5, "id": 1, "ataque": 50, "defensa": 30, "poder_magico": "pelea"},
            "jinete": {"vida": 80, "id": 2, "ataque": 40, "defensa": 20, "poder_magico": 5},
            "mago": {"vida": 60, "id": 3, "ataque": 20, "defensa": 10, "poder_magico": 60},
            "recolector": {"vida": 70, "id": 4, "ataque": 10, "defensa": 40, "poder_magico": 5},
            "observador": {"vida": 50, "id": 5, "ataque": 5, "defensa": 5, "poder_magico": 30}
        }
    },
    "Orcos": {
        "clases": ["guerrero", "chaman"],
        "atributos": {
            "guerrero": {"vida": 120, "id": 1, "ataque": 60, "defensa": 40, "poder_magico": 0},
            "chaman": {"vida": 80, "id": 2, "ataque": 30, "defensa": 20, "poder_magico": 50}
        }
    }
}


nombre_archivo = "informacion.json"


with open(nombre_archivo, "w") as archivo:
    json.dump(diccionario, archivo)

print("Archivo creado correctamente:")
print(json.dumps(diccionario, indent=4))