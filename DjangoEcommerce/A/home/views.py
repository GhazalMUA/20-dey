from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, template_name='home/home.html')
    
def navbarview(request):
    return render (request, 'inc/navbar.html')    

def baseview(request):
    return render (request, 'base.html')    