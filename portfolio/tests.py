from rest_framework.test import APITestCase
from rest_framework import status
from .models import Skill, Project, Blog, Newsletter


# Create your tests here.
class TestModels(APITestCase):
    def setUp(self):
        self.skill = Skill.objects.create(name='Django')
        self.project = Project.objects.create(
            category='Music',
            title='Sweet Sacrament Divine',
            description='SSD',
            link='https://google.com'
        )
        self.blog = Blog.objects.create(title='Cloudinary Django', body='I got the code')
        self.mail_list = Newsletter.objects.create(
            email='dflat1@outlook.com',
            first_name='Daniel',
            last_name='Azubuine'
        )

    def test_models(self):
        skill = self.skill
        project = self.project
        blog = self.blog
        mail_list = self.mail_list
        self.assertEqual(str(skill), 'Django')
        self.assertEqual(str(project), 'Sweet Sacrament Divine')
        self.assertEqual(str(blog), 'Cloudinary Django')
        self.assertEqual(str(mail_list), 'dflat1@outlook.com')

    def test_list_project(self):
        response = self.client.get('/api/projects/Music/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
