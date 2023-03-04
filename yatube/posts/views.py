from django.shortcuts import  HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Если честно хз что сюда писать')


def group_posts(request, pk):
    return HttpResponse(f'Оригинальный пост №{pk}')