from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from .models import Blog, BlogType#, ReadNum
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNum

# Create your views here.


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER) #每5篇进行分页
    page_num = request.GET.get('page', 1) #获取页面参数
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number
    #!!!
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(range(current_page_num, min(paginator.num_pages, current_page_num + 2) + 1))


    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')        

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取分类对应的数量
    '''
    blog_types = BlogType.objects.all()
    blog_types_list = []
    for blog_type in blog_types:
        blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
        blog_types_list.append(blog_type)
    '''
    # 上述方法等价于:
    # BlogType.objects.annotate(blog_count=Count('blog'))

    # 获取日期对应的数量
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    #context['blogs_count'] = Blog.objects.all().count()
    #context['blog_types'] = blog_types_list
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = blog_dates_dict

    return context

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)

    return render_to_response('blog/blog_list.html', context)

def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    
    return render_to_response('blog/blogs_with_type.html', context)

def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)

    return render_to_response('blog/blogs_with_date.html', context)

def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    if not request.COOKIES.get('blog_%s_readed' % blog_pk):
        ct = ContentType.objects.get_for_model(Blog)
        if ReadNum.objects.filter(content_type=ct, object_id=blog.pk).count():
            #存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=blog.pk)
        else:
            #不存在对应的记录
            readnum = ReadNum(content_type=ct, object_id=blog.pk)

        readnum.read_num += 1
        readnum.save()


    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog
    response = render_to_response('blog/blog_detail.html', context)
    response.set_cookie('blog_%s_readed' % blog_pk, 'true')
    return response