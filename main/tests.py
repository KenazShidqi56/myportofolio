from django.test import TestCase

# Create your tests here.
# tutorial 2...
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Education
from main.models import Skill
from main.models import Projects


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

        self.education = Education.objects.create(
            title="Labschool Jakarta Highschool",
            description="Study study study",
            category="highschool",
        )

        self.skill = Skill.objects.create(
            title="Java Program Language",
            description="I have learn this programming language in college.",
            category="hard skill",
        )

        self.projects = Projects.objects.create(
            title="Hackathon",
            description="We make an educational game app.",
            category="on-going",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    #Experience
    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    #education
    def test_education_model(self):
            self.assertEqual(str(self.education), "Labschool Jakarta Highschool")
            self.assertEqual(self.education.category, "highschool")
            self.assertTrue(self.education.is_ongoing)
    
    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.title)
        self.assertContains(response, self.education.description)
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_education(self):
        self.education.ended_at = timezone.now()
        self.education.save()
        response = self.client.get(reverse("main:show_education"))

        self.assertFalse(self.education.is_ongoing)
        self.assertNotContains(response, "Sedang berlangsung")

    #skill
    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Java Program Language")
        self.assertEqual(self.skill.category, "hard skill")
        self.assertTrue(self.skill.is_ongoing)

    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, self.skill.title)
        self.assertContains(response, self.skill.description)
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_skill(self):
        self.skill.ended_at = timezone.now()
        self.skill.save()
        response = self.client.get(reverse("main:show_skill"))

        self.assertFalse(self.skill.is_ongoing)
        self.assertNotContains(response, "Sedang berlangsung")

    #projects
    def test_projects_model(self):
        self.assertEqual(str(self.projects), "Hackathon")
        self.assertEqual(self.projects.category, "on-going")
        self.assertTrue(self.projects.is_ongoing)

    def test_projects_page(self):
        response = self.client.get(reverse("main:show_projects"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertContains(response, self.projects.title)
        self.assertContains(response, self.projects.description)
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_projects_page(self):
        Projects.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_projects(self):
        self.projects.ended_at = timezone.now()
        self.projects.save()
        response = self.client.get(reverse("main:show_projects"))

        self.assertFalse(self.projects.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")