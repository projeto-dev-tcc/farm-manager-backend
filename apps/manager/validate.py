from .models import Variedade
def validate_variedade(nome):
    try:
        variedade = Variedade.objects.get(nome__contains = nome)
        
        print("variedade")
        
        if variedade:
            return False
        return True
    except Variedade.DoesNotExist:
        return True