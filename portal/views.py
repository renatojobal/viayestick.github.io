from django.shortcuts import render_to_response
from portal import models
 
# View principal
def index(request):
    data_base_data =  {'data':'HOlaa'}
    return render_to_response('portal/index.html', context=data_base_data)
