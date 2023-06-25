from script import videomaker
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from db.models import Requests


def db_saver(req):
    request = Requests()
    request.request = req
    request.save()

def parser(request):
    if 'text' in request.GET:
        req = request.GET['text']
        db_saver(req)
        videomaker.make_video(req)
        file = FileWrapper(open('running_text.mp4', 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
        return response


def show_db(request):
    requests = Requests.objects.all()
    text = ""
    for elem in requests:
        text += elem.request
    return HttpResponse(text)
