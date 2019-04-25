from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    #form = UserCreationForm()
    return HttpResponse("Wow this is an strong tutorial")
    #return render(request,'users/register.html',{'form': form})



