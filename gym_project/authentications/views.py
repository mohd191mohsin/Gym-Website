from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request,'registration/register.html',{'form':form})