from django.shortcuts import render

def database(request):
    return render(request, 'main/index.html')
