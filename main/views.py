from django.shortcuts import render

# Create your views here.
# tutorial 2...
from django.shortcuts import render

from main.models import Experience
from main.models import Education
from main.models import Skill
from main.models import Projects


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

def show_education(request):
    context = {
        "name": "Kenaz Shidqi Baswara",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_skill(request):
    context = {
        "name": "Kenaz Shidqi Baswara",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skill.html", context)

def show_projects(request):
    context = {
        "name": "Kenaz Shidqi Baswara",
        "projects_list": Projects.objects.all(),
    }
    return render(request, "projects.html", context)