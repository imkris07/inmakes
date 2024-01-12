
from django.shortcuts import render
from . models import cars
from . models import client

# Create your views here.
def demo(request):
    obj=cars.objects.all()
    obj1=client.objects.all()

    return render(request, "index.html", {'result': obj, 'result1': obj1})

# #def addition(request):
#     #x=int(request.GET['num1'])
#     #y=int(request.GET['num2'])
#     #res=x+y
#     #return render(request, "about.html", {'result': res})
#
#
# #def names(request):
#     #return HttpResponse("hey dear")
