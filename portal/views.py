from django.shortcuts import render_to_response
from portal.models import Portal



# View principal
def index(request):
    
    # Aquí vamos a cargar los datos desde la base de datos

    query = Portal.objects.filter(name="Viayestick")[0]
    # Todo: Aquí debería cargarse todo el objeto pero quiero saber una forma fácil de hacerlo
    # ! Tal vez deba crear un serializador
    portal = {}


    return render_to_response('portal/index.html', context=portal)
