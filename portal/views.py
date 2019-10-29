from django.shortcuts import render_to_response
from portal import models



# View principal
def index(request):
    
    # Aquí vamos a cargar los datos desde la base de datos

    query = models.Portal.objects.filter(name="Viayestick")[0]
    

    data_base_data =  {'data':'Holaa'}
    return render_to_response('portal/index.html', context=data_base_data)
