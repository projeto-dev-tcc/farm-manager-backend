from apps.manager.models import Variedade

variedades = [
    ""
]

for variedade in variedades:
    obj = Variedade()
    obj.nome = variedade
    obj.save()