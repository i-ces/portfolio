from django.shortcuts import render
#for fetching data from database after this is included dictionary
#and jobs.object is written
from .models import job

def home(request):
    jobs = job.objects
    return render(request,'jobs/home.html', {'jobs':jobs})
