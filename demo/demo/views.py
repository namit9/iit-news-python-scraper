from django.http import HttpResponse

def index(request):
  f = open("../toi_organised.json","r")
  return HttpResponse(f, content_type="application/json")
