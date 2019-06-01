from django.shortcuts import render

from .models import LightBlog

# Create your views here.
def lightblog_list(request):
    context = {}
    context['lightblogs'] = LightBlog.objects.all()

    return render(request, 'lightblog/lightblog_list.html', context)