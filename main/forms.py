from django.forms.models import ModelForm
from django.forms.widgets import TextInput, Textarea, URLInput

from main.models import (
    Experience, 
    Education, 
    Skill, 
    Project
)

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "event_owner",
            "event_image_url",
        ]

        labels = {
            "title": "Your experience",
            "description": "Experience description",
            "event_owner": "Event Organizer",
            "event_image_url": "Picture URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "What is your experience?",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe this particular experience",
                    "rows": 3,
                }
            ),
            "event_owner": TextInput(
                attrs={
                    "placeholder": "The institution or company who runs this event",
                }
            ),
            "event_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "description",
            "education_level",
            "education_url",
            "education_image_url",
        ]

        labels = {
            "title": "School/University/Institution name",
            "description": "Description",
            "education_level": "Education level",
            "education_url": "URL Proyek",
            "education_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Tell where you study",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your education level experience",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Middleschool, Highschool, University",
                }
            ),
            "education_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/NealG/GreenProject",
                }
            ),
            "education_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "title",
            "description",
            "skill_category",
            "project_image_url",
        ]

        labels = {
            "title": "Skill You Master",
            "description": "Skill Description",
            "skill_category": "SKill Category",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "What skill do you have?",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "\"My skill can replace 5 employee\"",
                    "rows": 3,
                }
            ),
            "skill_category": TextInput(
                attrs={
                    "placeholder": "Soft skill or Hard skill",
                }
            ),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Project name",
            "description": "Project description",
            "tech_stack": "Technology used",
            "project_url": "Project URL",
            "project_image_url": "Picture URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Your project's title",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Technology you used for this project",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/NealG/GreenProject",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }