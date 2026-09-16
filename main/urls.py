from django.urls import path

from main.views import (
    get_projects_json,
    show_main, 
    show_experience, 
    show_education, 
    show_skill, 
    show_projects,
    create_project,
    delete_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("skill/", show_skill, name="show_skill"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),   #project_form
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
]