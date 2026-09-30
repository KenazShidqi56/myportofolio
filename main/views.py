# Create your views here.
# tutorial 4...
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

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

# tutorial 5...
from django.http import JsonResponse
from django.views.decorators.http import require_POST

"""
Authorization hierarchy:
[Owner]Create and delete
 [Editor]Update
  [Regular]Add star
   [Visitor]Read
"""

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "Kenaz Shidqi Baswara",
        "npm": "2506558144",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "\"I'm Kenaz, a computer science student. Currently this is my second year studying in Fasilkom UI. \
            For past months, I have been a mentor in faculty event and join programming competition. I find new friends \
            in every experience I join.\""
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)
# tutorial 2...
#EXPERIENCE SECTION...
def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Kenaz Shidqi Baswara",
        "title_query": title_query,
        "form": ExperienceForm,
    }
    return render(request, "experience.html", context)

# tutorial 3...
@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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
    experience = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    data = []
    for experience in experience:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_auhenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "event_owner": experience.event_owner,
                "event_image_url": experience.event_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "An experience has been deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def edit_experience(request, id):
    if not request.user.is_editor or request.user.is_superuser:
        raise PermissionDenied
    
    # Grab the exact experience by its UUID
    experience = get_object_or_404(Experience, pk=id)

    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Project, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

#EDUCATION SECTION...
def show_education(request):
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Kenaz Shidqi Baswara",
        "title_query": title_query,
        "form": EducationForm(),
    }
    return render(request, "education.html", context)

# tutorial 3...
@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
    education = Education.objects.prefetch_related('starred_by').all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    data = []
    for education in education:
        starred_users = education.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_auhenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(education.id),
            "fields": {
                "title": education.title,
                "description": education.description,
                "education_level": education.education_level,
                "education_url": education.project_url,
                "education_image_url": education.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "An education history has been deleted!")
        return redirect("main:show_education")

    return redirect("main:show_education")

@login_required(login_url="/login/")
def edit_education(request, id):
    if not request.user.is_editor or request.user.is_superuser:
        raise PermissionDenied

    # Grab the exact experience by its UUID
    education = get_object_or_404(Education, pk=id)

    form = EducationForm(request.POST or None, instance=education)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_education')
    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def toggle_star_education(request, education_id):
    education = get_object_or_404(Project, pk=education_id)

    if request.method == "POST":
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_education")

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

#SKILL SECTION...
def show_skill(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Kenaz Shidqi Baswara",
        "title_query": title_query,
        "form": SkillForm(),
    }
    return render(request, "skill.html", context)

@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
    skill = Skill.objects.prefetch_related('starred_by').all()

    if title_query:
        skill = skill.filter(title__icontains=title_query)

    data = []
    for skill in skill:
        starred_users = skill.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_auhenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(skill.id),
            "fields": {
                "title": skill.title,
                "description": skill.description,
                "skill_category": skill.skill_category,
                "skill_image_url": skill.skill_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "A skill has been deleted!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")

@login_required(login_url="/login/")
def edit_skill(request, id):
    if not request.user.is_editor or request.user.is_superuser:
        raise PermissionDenied

    # Grab the exact experience by its UUID
    skill = get_object_or_404(Skill, pk=id)

    form = SkillForm(request.POST or None, instance=skill)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_skill')
    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "skill_form.html", context)

@login_required(login_url="/login/")
def toggle_star_skill(request, skill_id):
    skill = get_object_or_404(Project, pk=skill_id)

    if request.method == "POST":
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)

    return redirect("main:show_skill")

@require_POST
def create_skil_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = SkillForm(request.POST)
    if form.is_valid():
        skill = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(skill.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

#PROJECT SECTION...
def show_project(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Kenaz Shidqi Baswara",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

# tutorial 3...
@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
    project = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        project = project.filter(title__icontains=title_query)

    data = []
    for project in project:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_auhenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "A project has been deleted!")
        return redirect("main:show_project")

    return redirect("main:show_project")

@login_required(login_url="/login/")
def edit_project(request, id):
    if not request.user.is_editor or request.user.is_superuser:
        raise PermissionDenied
    
    # Grab the exact experience by its UUID
    project = get_object_or_404(Project, pk=id)

    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_project')
    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }
    return render(request, "project_form.html", context)

@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

# AUTHENTICATION...
def register (request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in!")
        return redirect("main.login")

    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }

    return render(request, "register.html", context)

def login_user (request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%d/%m %Y [%H: %M: %S]'))
        return response

    context = {
        "name": "Kenaz Shidqi Baswara",
        "form": form,
    }

    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return redirect("main:show_main")