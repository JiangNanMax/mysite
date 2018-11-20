def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)

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