from django.shortcuts import render_to_response
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import get_week_read_data, get_week_hot_data
from blog.models import Blog

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_week_read_data(blog_content_type)
    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['week_hot_data'] = get_week_hot_data(blog_content_type)
    return render_to_response('home.html', context)