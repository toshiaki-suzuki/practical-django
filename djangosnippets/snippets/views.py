from django.http import HttpResponse


def top(request):
    return HttpResponse('Hello World')
