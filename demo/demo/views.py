from django.http import HttpResponse
from constants import iit_list

import json

def index(request):
  f = open("./../toi_organised.json","r")
  return HttpResponse(f, content_type="application/json")

def api(request):
  list_iits = request.GET.getlist('iit', None)
  if not list_iits:
    list_iits = iit_list
  count = int(request.GET.get('items', -1))
  with open("./../toi_organised.json", "r") as f:
    data = json.load(f)
  result = {}
  for iit in list_iits:
    if count > len(data[iit]) or count == -1:
      result[iit] = data[iit]
    else:
      result[iit] = data[iit][:count-1]
    
  return HttpResponse(json.dumps(result), content_type="application/json")
