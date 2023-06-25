from script import videomaker
from wsgiref.util import FileWrapper
from django.http import HttpResponse

def parser(request):
    if 'text' in request.GET:
        videomaker.make_video(request.GET['text'])
        file = FileWrapper(open('running_text.mp4', 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
        return response
