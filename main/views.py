from django.shortcuts import render

# Create your views here.
# tutorial 2...
from django.shortcuts import render

from main.forms import ProjectForm
from main.models import Experience
from main.models import Education
from main.models import Skill
from main.models import Projects

# Tutorial 3...
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Kenaz Shidqi Baswara",
        "projects_list": Projects.objects.all(),
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

# tutorial 3...
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")