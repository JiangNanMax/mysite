from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime
from django.db.models import Sum
from .models import ReadNum, ReadDetail

def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        '''
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            #存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            #不存在对应的记录
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        '''
        # 上述代码等价于：
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)

        readnum.read_num += 1
        readnum.save()


        date = timezone.now().date()
        '''
        if ReadDetail.objects.filter(content_type=ct, object_id=obj.pk, date=date):
            readDetail = ReadDetail.objects.get(content_type=ct, object_id=obj.pk, date=date)
        else:
            readDetail = ReadDetail(content_type=ct, object_id=obj.pk, date=date)
        '''
        readDetail, created =  ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)

        readDetail.read_num += 1
        readDetail.save()
    return key

def get_week_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums