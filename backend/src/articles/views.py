import os,json
from django.http import JsonResponse
from django.conf import settings


def index(request):
    file_ = open(os.path.join(settings.BASE_DIR, 'query_specs.json'))
    query_data = json.load(file_)
    q = request.GET.get('q', None)
    results = {k: v for k, v in query_data.items(
    ) if q is None or q.lower() in k.lower()}
    return JsonResponse(results)
