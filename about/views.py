from django.shortcuts import render

# Create your views here.
def aboutme(request):
    return render(request, 'about/aboutme.html')

