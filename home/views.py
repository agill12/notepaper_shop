from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
def get_index(request):
    return render(request,'home/index.html')