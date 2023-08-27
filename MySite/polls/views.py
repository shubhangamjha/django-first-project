from django.shortcuts import render

# Create your views here.
from . import models
from .models import Question


def index(request):

    q= Question.objects.all()
    return render(request, 'index.html', {"questions" : q, "Lang":"PYTHON"})