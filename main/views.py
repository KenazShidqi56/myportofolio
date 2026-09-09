from django.shortcuts import render

# Create your views here.
# tutorial 2...
from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Kenaz Shidqi Baswara",
        "npm": "2506558144",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "\"I'm Kenaz, a computer science student. Currently this is my second year studying in Fasilkom UI. \
            For past months, I have been a mentor in faculty event and join programming competition. I find new friends in every experience I join.\""
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Kenaz Shidqi Baswara",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)