from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import wenzhang


def index(request):
    #return HttpResponse("HELLO! This is myapp1")
    return render(request, "myapp1/index.html")

def test(request):
    context = {"name": "wzr", "age": "37"}
    return render(request, "test.html", context)


def get_wenzhang(request):
    content = {"content": wenzhang.objects.get(id=1)}
    # objects.all()
    return render(request, 'news.html', content)


# return HttpResponse(content)
def news_list(request):
    list = wenzhang.objects.all().values()
    context = {'list': list,
               }
    return render(request, 'news_list.html', context)
