from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.

def create_stud(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=="POST":
        SDFO=StudentForm(request.POST)
        if SDFO.is_valid():
            sid=SDFO.cleaned_data['student_id']
            snm=SDFO.cleaned_data['student_name']
            sage=SDFO.cleaned_data['student_age']
            sem=SDFO.cleaned_data['student_email']
            SO=Student.objects.get_or_create(sid=sid,sname=snm,sage=sage,em=sem)[0]
            SO.save()
            return HttpResponse("Data inserted")
            #return HttpResponse(str(SDFO.cleaned_data))
        else:
            return HttpResponse('Invalid Data')
    return render(request,"create_stud.html",d)