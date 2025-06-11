from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World, bks4kids - books for childrene - reviews")