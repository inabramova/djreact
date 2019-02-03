from django.shortcuts import render
from django.http import JsonResponse
import json


def index(request):
    with open('/home/inabramova/Downloads/query_specs.json') as f:
        query_data = json.load(f)
    q = request.GET.get('q', None)
    results = {k: v for k, v in query_data.items(
    ) if q is None or q.lower() in k.lower()}
    """ res=[]
    for title_key, rec in results.items():
        res.append({**rec,**{'title':title_key}})
    print(res) """
    return JsonResponse(results)
