from django.shortcuts import render
from django.views import View
# Create your views here.

class ghazal(View):
    def get(self,request):
        return render(request,'ghazal.html')


class 