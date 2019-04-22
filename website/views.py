from django.shortcuts import render


# Create your views here.
def demo(request):
    return render(request, 'website/demo.html')


# def index(request):
#     return render(request, 'website/index.html')
