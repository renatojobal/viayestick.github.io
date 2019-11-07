from django.shortcuts import render_to_response
from portal.models import Portal, Review, External_link



# View principal
def index(request):

    context = {}

    # Aquí vamos a cargar los datos desde la base de datos

    portal = Portal.objects.filter(name="Viayestick").get()
    reviews = Review.objects.filter(portal=portal)
    external_links = External_link.objects.filter(portal=portal)


    context['portal'] = portal


    return render_to_response('portal/index.html', context=context)
