from django.http import HttpResponse 
from django.shortcuts import render

def index1(request):
    return HttpResponse('greetings from the onlineapp')
def index2(request):
    return render(request, 'shajil1.html')    


