from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
from django.contrib import auth
from django.db.models import Sum
from django.core.cache import cache
from django.urls import reverse
from read_statistics.utils import get_week_read_data
from blog.models import Blog


def get_week_hot_data():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    #???
    blogs = Blog.objects.filter(read_details__date__lt=today, read_details__date__gte=date).values('id', 'title').annotate(read_num_sum=Sum('read_details__read_num')).order_by('-read_num_sum')
    return blogs[:8]

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_week_read_data(blog_content_type)

    # 获取缓存数据
    week_hot_data = cache.get('week_hot_data')
    if week_hot_data is None:
        week_hot_data = get_week_hot_data()
        cache.set('week_hot_data', week_hot_data, 3600)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['week_hot_data'] = week_hot_data
    return render(request, 'home.html', context)

def login(request):
    '''
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if user is not None:
        auth.login(request, user)
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': 'wrong username or password.'})
    '''
    return render(request, 'login.html', {})