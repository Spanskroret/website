from django.shortcuts import render

# Create your views here.
def spanky(request):
    return render(request,'spanky/index.html')