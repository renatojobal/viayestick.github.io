from django.shortcuts import render_to_response
 
# View principal
def index(request):
    return render_to_response('portal/index.html')
