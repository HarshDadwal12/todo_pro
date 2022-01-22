from django.shortcuts import redirect, render


from todo_app.serializers import ListSerializers
from .models import List
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
## for displaying all the content of To-Do List 
def home(request):
    all_item=List.objects.all()
    return render(request,'home.html',{'all_items':all_item})

## For Creating crud functionality and authenticate user with session authentications, limit user to visit site by throttling
class ListCRUD(viewsets.ModelViewSet):
    queryset=List.objects.all()
    serializer_class=ListSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]

def done(request,id):
    data=List.objects.get(pk=id)
    data.status=True
    data.save()
    return redirect('home')

def undone(request,id):
    data=List.objects.get(pk=id)
    data.status=False
    data.save()
    return redirect('home')

'''super user-harsh
password- harsh'''

