from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

#from .models import Register
#from .models import Doctor
#from .models import IsIt


def index(request):
#    latest = Register.objects.order_by('-dt')[:5]
#    latest = Register.objects.all()
#    lat_doc = Doctor.objects.all()
#    tt = IsIt.objects.all()
#    context = {'latest': latest, 'lat_doc': lat_doc, 'time': tt}
    if request.method == 'GET':
        return render(request, 'form.html')#, context)
    elif request.method == 'POST':
        Name = request.POST['element_1_1']
        Surname = request.POST['element_1_2']
        Doctor = request.POST['element_3']
        tm = request.POST['element_4']
        dt = '/'.join([request.POST['element_2_1'], request.POST['element_2_2'], request.POST['element_2_3']])
        context = {'name': Name, 'surname': Surname, 'doctor': Doctor, 'tm': tm, 'dt': dt, 'test': "test"}
        return render(request, 'done.html', context)
