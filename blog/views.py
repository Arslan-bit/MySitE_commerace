from django.shortcuts import render


def index(request):
    # return HttpResponse("Index blog")
    return render(request, 'blog/index_html.html')
