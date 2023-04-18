from django.shortcuts import render

from ui.models import category


# Create your views here.
def home(request):
    Subjects = category.objects.all()
    context = {
        "Subjects": Subjects
    }
    return render(request, 'home.html' , context)
