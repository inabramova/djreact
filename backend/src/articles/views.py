import os,json
import time
from datetime import datetime
from django.http import JsonResponse
from django.conf import settings

def convert_time(str):
    try:
        date_obj = datetime.strptime(str,'%m/%d/%Y:%H:%M:%S')
        return int(time.mktime(date_obj.timetuple())) * 1000
    except ValueError:
        return str

def check_dates(rec):
    rec['date_filters'] = [[convert_time(fltr) for fltr in fltrs] for fltrs in rec['date_filters']]
    return rec

def index(request):
    file_ = open(os.path.join(settings.BASE_DIR, 'query_specs.json'))
    query_data = json.load(file_)
    q = request.GET.get('q', None)
    results = {k: check_dates(v) for k, v in query_data.items(
    ) if q is None or q.lower() in k.lower()}
    return JsonResponse(results)
