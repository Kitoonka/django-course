from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('testing.html')  # or your template name
    context = {
        'firstname': 'Steve',
    }
    return HttpResponse(template.render(context, request))