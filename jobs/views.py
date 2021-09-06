from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects #getting all job objects from jobs model
    return render(request, 'jobs/home.html', {'jobs': jobs})