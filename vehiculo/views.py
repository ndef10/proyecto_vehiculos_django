from django.shortcuts import render

# Create your views here.
def v_index(request):
    return render(request, 'vehiculos/index.html')
