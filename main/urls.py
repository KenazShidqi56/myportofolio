from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    get_experience_json,
    create_experience,
    delete_experience,
    edit_experience,
    toggle_star_experience,
    create_experience_ajax,

    show_education, 
    get_education_json,
    create_education,
    delete_education,
    edit_education,
    toggle_star_education,
    create_education_ajax,

    show_skill, 
    get_skill_json,
    create_skill,
    delete_skill,
    edit_skill,
    toggle_star_skill,
    create_skil_ajax,

    show_project,
    get_project_json,
    create_project,
    delete_project,
    edit_project,
    toggle_star_project,
    create_project_ajax,

    register,
    login_user,
    logout_user,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),   #experience_form
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<str:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),

    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),   #education_form
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("education/<str:id>/edit/", edit_education, name="edit_education"),
    path("education/<uuid:education_id>/star/", toggle_star_education, name="toggle_star_education"),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),

    path("skill/", show_skill, name="show_skill"),
    path("skill/add/", create_skill, name="create_skill"),   #skill_form
    path("api/skill/", get_skill_json, name="get_skill_json"),
    path("skill/<uuid:skill_id>/skill/", delete_skill, name="delete_skill"),
    path("skill/<str:id>/edit/", edit_skill, name="edit_skill"),
    path("skill/<uuid:skill_id>/star/", toggle_star_skill, name="toggle_star_skill"),
    path("skill/add-ajax/", create_skil_ajax, name="create_skill_ajax"),

    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),   #project_form
    path("api/project/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("project/<str:id>/edit/", edit_project, name="edit_project"),
    path("project/<uuid:project_id>/star/", toggle_star_project, name="toggle_star_project"),
    path("project/add-ajax/", create_project_ajax, name="create_project_ajax"),

    path("register/", register, name="register"),
    path("register/main.login", show_main, name="register_to_main"),
    path("login/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout_user"),
]

#NOTE: add new function from views to "urlpatterns"