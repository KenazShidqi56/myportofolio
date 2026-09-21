from django.shortcuts import render

# Create your views here.
# tutorial 2...
from django.shortcuts import render

from main.forms import (
    ExperienceForm, 
    EducationForm, 
    SkillForm, 
    ProjectForm,
)

from main.models import (
    Experience, 
    Education, 
    Skill, 
    Project,
)

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

#EXPERIENCE SECTION...
def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience = [experience.object for experience in experience]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Kenaz Shidqi Baswara",
        "experience_list": Experience.objects.all(),
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

# tutorial 3...
def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience succesfully added!")
        return redirect("main:show_experience")

    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "An experience has been deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

#EDUCATION SECTION...
def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education = [education.object for education in education]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Kenaz Shidqi Baswara",
        "education_list": Education.objects.all(),
        "title_query": title_query,
    }
    return render(request, "education.html", context)

# tutorial 3...
def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New education history succesfully added!")
        return redirect("main:show_education")

    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "An education history has been deleted!")
        return redirect("main:show_education")

    return redirect("main:show_education")

#SKILL SECTION...
def show_skill(request):
    json_response = get_skill_json(request)

    skill = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skill = [skill.object for skill in skill]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Kenaz Shidqi Baswara",
        "skill_list": Skill.objects.all(),
        "title_query": title_query,
    }
    return render(request, "skill.html", context)

def create_skill(request):
    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New skill succesfully added!")
        return redirect("main:show_skill")

    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "skill_form.html", context)

def get_skill_json(request):
    title_query = request.GET.get("title", "").strip()
    skill = Skill.objects.all()

    if title_query:
        skill = skill.filter(title__icontains=title_query)

    skill_json = serializers.serialize("json", skill)
    return HttpResponse(skill_json, content_type="application/json")

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "A skill has been deleted!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")

#PROJECT SECTION...
def show_project(request):
    json_response = get_project_json(request)

    project = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    project = [project.object for project in project]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Kenaz Shidqi Baswara",
        "project_list": Project.objects.all(),
        "title_query": title_query,
    }
    return render(request, "project.html", context)

# tutorial 3...
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project succesfully added!")
        return redirect("main:show_project")

    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "project_form.html", context)

def get_project_json(request):
    title_query = request.GET.get("title", "").strip()
    project = Project.objects.all()

    if title_query:
        project = project.filter(title__icontains=title_query)

    project_json = serializers.serialize("json", project)
    return HttpResponse(project_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "A project has been deleted!")
        return redirect("main:show_project")

    return redirect("main:show_project")